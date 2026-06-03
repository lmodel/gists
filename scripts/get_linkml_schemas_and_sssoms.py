#!/usr/bin/env python3
"""
get-linkml-schemas-and-sssoms.py

Iterates over all repos in a GitHub organization and downloads:
  - src/<snake_case(repo_name)>/schema/*.yaml
  - src/<snake_case(repo_name)>/mappings/*.sssom.tsv

Flattened output layout:
  downloaded-artifacts/<org>/<filename>

Optional:
  --index <path> writes a CSV index (repo, original_path, download_url, saved_as, sha, ...)

Usage:
  python get-linkml-schemas-and-sssoms.py                 # defaults to org 'lmodel'
  python get-linkml-schemas-and-sssoms.py myorg
  python get-linkml-schemas-and-sssoms.py myorg --out ./downloaded-artifacts
  python get-linkml-schemas-and-sssoms.py myorg --index ./downloaded-artifacts/myorg/index.csv
  GITHUB_TOKEN=... python get-linkml-schemas-and-sssoms.py myorg --index index.csv

Notes:
- Uses GitHub REST API v3.
- If you set GITHUB_TOKEN (recommended), you get higher rate limits.
"""

import argparse
import csv
import os
import re
import sys
import time
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple, Union

import requests


GITHUB_API = "https://api.github.com"
DEFAULT_ORG = "lmodel"


def snake_case(name: str) -> str:
    """
    Convert repo name to snake_case.
    """
    s = name.strip()
    s = re.sub(r"[.\- ]+", "_", s)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    s = re.sub(r"__+", "_", s)
    return s.lower()


def gh_headers(token: Optional[str]) -> Dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "get-linkml-schemas-and-sssoms",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def request_json(url: str, headers: Dict[str, str], params: Optional[dict] = None, timeout: int = 30):
    """
    GitHub API GET with simple retry/backoff for rate limiting.
    """
    backoff = 2
    r = None

    for _attempt in range(1, 6):
        r = requests.get(url, headers=headers, params=params, timeout=timeout)

        # Handle rate limiting / secondary throttling
        if r.status_code == 403:
            remaining = r.headers.get("X-RateLimit-Remaining")
            reset = r.headers.get("X-RateLimit-Reset")
            msg = r.text[:300].replace("\n", " ")

            # Primary rate limit
            if remaining == "0" and reset:
                sleep_for = max(1, int(reset) - int(time.time()) + 2)
                print(f"[rate-limit] Sleeping {sleep_for}s until reset... ({msg})", file=sys.stderr)
                time.sleep(sleep_for)
                continue

            # Secondary rate limit or other 403
            print(f"[throttle] 403 from GitHub; backing off {backoff}s... ({msg})", file=sys.stderr)
            time.sleep(backoff)
            backoff *= 2
            continue

        if r.status_code in (500, 502, 503, 504):
            print(f"[server] {r.status_code}; retrying in {backoff}s...", file=sys.stderr)
            time.sleep(backoff)
            backoff *= 2
            continue

        if not r.ok:
            return r, None

        return r, r.json()

    return r, None


def list_org_repos(org: str, headers: Dict[str, str]) -> List[dict]:
    """
    List all repos for an org, handling pagination.
    """
    repos: List[dict] = []
    page = 1
    per_page = 100

    while True:
        url = f"{GITHUB_API}/orgs/{org}/repos"
        r, data = request_json(url, headers, params={"per_page": per_page, "page": page, "type": "all"})
        if not r.ok:
            raise RuntimeError(f"Failed to list repos for org '{org}': {r.status_code} {r.text}")

        if not data:
            break

        repos.extend(data)
        if len(data) < per_page:
            break
        page += 1

    return repos


def get_contents(owner: str, repo: str, path: str, headers: Dict[str, str]) -> Tuple[int, Optional[Union[dict, list]]]:
    """
    Get GitHub repo contents at a path.
    Returns (status_code, json_data_or_none).
    """
    url = f"{GITHUB_API}/repos/{owner}/{repo}/contents/{path}"
    r, data = request_json(url, headers)
    return r.status_code, data


def iter_matching_files(owner: str, repo: str, start_path: str, headers: Dict[str, str], match_fn) -> Iterable[dict]:
    """
    Recursively traverse a directory tree starting at start_path, yielding file objects
    whose name satisfies match_fn(file_obj).

    If start_path doesn't exist, yields nothing.
    """
    status, data = get_contents(owner, repo, start_path, headers)
    if status == 404 or data is None:
        return
    if status != 200:
        print(f"[warn] {owner}/{repo}: cannot read '{start_path}' (HTTP {status})", file=sys.stderr)
        return

    stack: List[Union[dict, list]] = [data]

    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            if node.get("type") == "file" and match_fn(node):
                yield node
            continue

        for item in node:
            t = item.get("type")
            if t == "file":
                if match_fn(item):
                    yield item
            elif t == "dir":
                sub_path = item.get("path")
                st, sub_data = get_contents(owner, repo, sub_path, headers)
                if st == 200 and sub_data is not None:
                    stack.append(sub_data)
                elif st != 404:
                    print(f"[warn] {owner}/{repo}: cannot read dir '{sub_path}' (HTTP {st})", file=sys.stderr)


def _full_suffix(name: str) -> str:
    """
    Return full suffix including multi-part extensions:
      foo.sssom.tsv -> .sssom.tsv
      bar.yaml -> .yaml
    """
    p = Path(name)
    return "".join(p.suffixes) if p.suffixes else ""


def unique_dest_path(dest_dir: Path, filename: str, repo_name: str) -> Path:
    """
    Compute a destination path in dest_dir for filename.
    If a file already exists, avoid overwriting by suffixing with repo_name and/or counter.
    """
    dest = dest_dir / filename
    if not dest.exists():
        return dest

    stem = Path(filename).name
    suffix = _full_suffix(filename)
    base = stem[: -len(suffix)] if suffix and stem.endswith(suffix) else Path(filename).stem

    alt = dest_dir / f"{base}__{repo_name}{suffix}"
    if not alt.exists():
        return alt

    i = 2
    while True:
        candidate = dest_dir / f"{base}__{repo_name}__{i}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def download_file_flat(file_obj: dict, headers: Dict[str, str], dest_dir: Path, repo_name: str) -> Optional[Path]:
    """
    Download a GitHub content file (via download_url) to dest_dir/<filename> (flattened).
    Returns local path if downloaded; otherwise None.
    """
    download_url = file_obj.get("download_url")
    filename = file_obj.get("name")
    if not download_url or not filename:
        return None

    dest_dir.mkdir(parents=True, exist_ok=True)
    local_path = unique_dest_path(dest_dir, filename, repo_name)

    with requests.get(download_url, headers=headers, stream=True, timeout=60) as r:
        if not r.ok:
            print(f"[warn] download failed: {download_url} -> HTTP {r.status_code}", file=sys.stderr)
            return None
        with open(local_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 64):
                if chunk:
                    f.write(chunk)

    return local_path


def open_index_writer(index_path: Path) -> Tuple[csv.DictWriter, object]:
    """
    Opens CSV index file for append; writes header if file doesn't exist.
    Returns (writer, file_handle) so caller can close handle.
    """
    index_path.parent.mkdir(parents=True, exist_ok=True)
    file_exists = index_path.exists()

    fh = open(index_path, "a", newline="", encoding="utf-8")
    fieldnames = ["repo", "artifact_type", "original_path", "download_url", "saved_as", "sha"]
    writer = csv.DictWriter(fh, fieldnames=fieldnames)

    if not file_exists:
        writer.writeheader()

    return writer, fh


def infer_artifact_type(file_obj: dict) -> str:
    name = (file_obj.get("name") or "").lower()
    if name.endswith(".sssom.tsv"):
        return "sssom_tsv"
    if name.endswith(".yaml"):
        return "schema_yaml"
    return "unknown"


def main():
    parser = argparse.ArgumentParser(
        description="Download LinkML schema YAMLs and SSSOM mapping TSV artifacts from all repos in a GitHub org."
    )
    parser.add_argument(
        "organization",
        nargs="?",
        default=DEFAULT_ORG,
        help=f"GitHub organization to scan (default: {DEFAULT_ORG})",
    )
    parser.add_argument(
        "--out",
        default="./downloaded-artifacts",
        help="Output directory root (default: ./downloaded-artifacts)",
    )
    parser.add_argument(
        "--token",
        default=os.environ.get("GITHUB_TOKEN"),
        help="GitHub token (or set env var GITHUB_TOKEN). Strongly recommended to avoid rate limiting.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only list matching files; do not download.",
    )
    parser.add_argument(
        "--index",
        default=None,
        help="Optional CSV index file path (e.g., ./downloaded-artifacts/<org>/index.csv). "
             "If provided, writes a row per downloaded artifact.",
    )

    args = parser.parse_args()

    org = args.organization
    out_root = Path(args.out).resolve()
    org_out = out_root / org  # flattened: everything goes here
    org_out.mkdir(parents=True, exist_ok=True)

    headers = gh_headers(args.token)

    print(f"[info] Scanning organization: {org}")
    if args.token:
        print("[info] Using GITHUB_TOKEN for authenticated API calls.")
    else:
        print("[info] No token provided; you may hit GitHub API rate limits.", file=sys.stderr)

    repos = list_org_repos(org, headers)
    print(f"[info] Found {len(repos)} repos.")
    print(f"[info] Output directory: {org_out}")

    index_writer = None
    index_fh = None
    if args.index and not args.dry_run:
        index_path = Path(args.index).resolve()
        index_writer, index_fh = open_index_writer(index_path)
        print(f"[info] Writing index CSV: {index_path}")
    elif args.index and args.dry_run:
        print("[info] --index ignored because --dry-run is enabled.")

    total_matches = 0
    total_downloaded = 0

    try:
        for repo in repos:
            repo_name = repo.get("name")
            if not repo_name:
                continue

            snake = snake_case(repo_name)
            schema_path = f"src/{snake}/schema"
            mappings_path = f"src/{snake}/mappings"

            def is_schema_yaml(fobj: dict) -> bool:
                return (fobj.get("name") or "").endswith(".yaml")

            def is_sssom_tsv(fobj: dict) -> bool:
                return (fobj.get("name") or "").endswith(".sssom.tsv")

            schema_files = list(iter_matching_files(org, repo_name, schema_path, headers, is_schema_yaml))
            mapping_files = list(iter_matching_files(org, repo_name, mappings_path, headers, is_sssom_tsv))

            matched = schema_files + mapping_files
            if not matched:
                continue

            print(f"\n[repo] {repo_name}")
            print(f"  snake_case: {snake}")
            print(f"  schema dir: {schema_path} -> {len(schema_files)} match(es)")
            print(f"  mappings dir: {mappings_path} -> {len(mapping_files)} match(es)")

            total_matches += len(matched)

            for fobj in matched:
                rel_path = fobj.get("path")
                fname = fobj.get("name")
                sha = fobj.get("sha")
                download_url = fobj.get("download_url")
                artifact_type = infer_artifact_type(fobj)

                if args.dry_run:
                    print(f"   [match] {rel_path}  ->  {fname}")
                    continue

                local = download_file_flat(fobj, headers, org_out, repo_name)
                if local:
                    total_downloaded += 1
                    print(f"   [downloaded] {rel_path} -> {local}")

                    if index_writer:
                        index_writer.writerow({
                            "repo": repo_name,
                            "artifact_type": artifact_type,
                            "original_path": rel_path or "",
                            "download_url": download_url or "",
                            "saved_as": str(local),
                            "sha": sha or "",
                        })
                else:
                    print(f"   [warn] could not download {rel_path}", file=sys.stderr)

    finally:
        if index_fh:
            index_fh.close()

    print("\n[done]")
    print(f"  Total matching files: {total_matches}")
    if not args.dry_run:
        print(f"  Total downloaded files: {total_downloaded}")
        print(f"  Output root: {org_out}")


if __name__ == "__main__":
    main()
