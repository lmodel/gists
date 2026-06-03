#!/usr/bin/env python3
"""Overlay SSSOM mappings onto LinkML schema YAML files.

Schema-independent: subject-side CURIE prefixes are derived automatically
from each schema's own ``name`` / ``default_prefix``, or may be supplied
explicitly via ``--subject-prefix`` (repeatable).

For every class / enum / type / slot whose unsuffixed local name appears as
a subject in one of the SSSOM TSVs, the script merges predicate-mapped
CURIEs into the matching mapping slot (``exact_mappings``,
``close_mappings``, ``broad_mappings``, ``narrow_mappings``,
``related_mappings``). Existing entries are preserved; duplicates dropped.
Object-side prefixes referenced by the merged CURIEs are added to the
schema's ``prefixes`` block (URIs come from each TSV's ``#curie_map:``
metadata).

The YAML is rewritten with ruamel.yaml in round-trip mode so comments and
folded block scalars in the source schema are preserved.

Usage::

    python scripts/apply_sssom_overlay.py \\
        --schema-dir src/<project>/schema \\
        --mappings-dir src/<project>/mappings

    # Or target a single schema file with explicit subject prefixes:
    python scripts/apply_sssom_overlay.py \\
        --schema src/iso27001/schema/iso27001.yaml \\
        --mappings-dir src/iso27001/mappings \\
        --subject-prefix iso27001

The script is idempotent: running it twice on a clean tree is a no-op.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from ruamel.yaml import YAML
    from ruamel.yaml.comments import CommentedMap, CommentedSeq
except ImportError as exc:
    sys.stderr.write(
        "ERROR: this script requires the 'ruamel.yaml' package, which is not "
        "installed in the current Python environment.\n"
        f"  (import failed: {exc})\n"
        "\n"
        "To install it, choose one of:\n"
        "  - uv add ruamel.yaml                          "
        "# add as a project dep\n"
        "  - uv pip install ruamel.yaml                  "
        "# install into the active venv\n"
        "  - pip install ruamel.yaml                     "
        "# plain pip\n"
        "\n"
        "Or run this script ad-hoc without installing:\n"
        "  uv run --with ruamel.yaml python scripts/apply_sssom_overlay.py ...\n"
    )
    sys.exit(2)

import yaml as _pyyaml  # only for parsing the leading TSV #-metadata block


# SKOS / OWL predicate -> LinkML mapping slot.
SSSOM_PREDICATE_TO_LINKML_SLOT: dict[str, str] = {
    "skos:exactMatch":         "exact_mappings",
    "skos:closeMatch":          "close_mappings",
    "skos:broadMatch":          "broad_mappings",
    "skos:narrowMatch":         "narrow_mappings",
    "skos:relatedMatch":        "related_mappings",
    "owl:equivalentClass":      "exact_mappings",
    "owl:equivalentProperty":   "exact_mappings",
}

# Prefixes intrinsic to LinkML / SSSOM; never need to be declared on a schema.
_BUILTIN_PREFIXES = {
    "sssom", "owl", "rdf", "rdfs", "skos", "semapv", "linkml", "xsd", "dcterms",
}

_MAPPING_SLOT_ORDER = (
    "exact_mappings",
    "close_mappings",
    "broad_mappings",
    "narrow_mappings",
    "related_mappings",
)

# Where mapping slots should sit within an element body (used only when none
# of the five mapping slots are present yet, so we know where to splice).
_POST_MAPPING_ANCHORS = (
    "aliases", "in_subset", "permissible_values", "attributes", "slots",
    "slot_usage", "rules", "comments", "annotations", "pattern",
)


# ---------------------------------------------------------------------------
# SSSOM TSV parsing
# ---------------------------------------------------------------------------


def _parse_sssom_metadata(path: Path) -> dict:
    """Parse the leading ``#`` metadata block of an SSSOM TSV as YAML.

    Falls back to a line-by-line extraction of the ``curie_map:`` block when
    the full metadata is not valid YAML (e.g. unquoted colons in URI values).
    """
    buf: list[str] = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("#"):
                break
            buf.append(line[1:])
    if not buf:
        return {}
    try:
        meta = _pyyaml.safe_load("".join(buf))
        return meta if isinstance(meta, dict) else {}
    except _pyyaml.YAMLError as exc:
        print(
            f"WARN: {path.name} metadata block is not valid YAML "
            f"({exc.problem!r} at line {exc.problem_mark.line + 1 if exc.problem_mark else '?'}); "
            f"falling back to line-by-line curie_map extraction. "
            f"Fix the metadata block to eliminate this warning.",
            file=sys.stderr,
        )

    # Fallback: extract only the curie_map block via simple line scanning.
    curie_map: dict[str, str] = {}
    in_curie_map = False
    for raw_line in buf:
        line = raw_line.rstrip()
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        if stripped == "curie_map:":
            in_curie_map = True
            curie_map_indent: int | None = None
            continue
        if in_curie_map:
            if not stripped or (curie_map_indent is not None and indent <= 0):
                # Blank line or back to top level — end of block.
                if indent == 0 and stripped:
                    break
                if not stripped:
                    continue
            if curie_map_indent is None:
                curie_map_indent = indent
            if indent < curie_map_indent:
                break  # dedented past the block
            if ":" in stripped:
                key, _, val = stripped.partition(":")
                val = val.strip().strip('"').strip("'")
                if key and val:
                    curie_map[key.strip()] = val
    return {"curie_map": curie_map} if curie_map else {}


def _parse_sssom_rows(path: Path) -> tuple[list[str], list[list[str]]]:
    """Return ``(header, rows)`` from the TSV body (skipping metadata)."""
    header: list[str] | None = None
    rows: list[list[str]] = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\r\n")
            if not line or line.startswith("#"):
                continue
            fields = line.split("\t")
            if header is None:
                header = fields
                continue
            rows.append(fields)
    return (header or []), rows


# ---------------------------------------------------------------------------
# Mapping index
# ---------------------------------------------------------------------------


class MappingIndex:
    """Holds all raw SSSOM rows plus a per-schema, prefix-filtered view."""

    def __init__(self) -> None:
        self.by_name: dict[str, dict[str, list[str]]] = {}
        self.prefix_uris: dict[str, str] = {}
        self.rows: list[tuple[str, str, str]] = []  # (subject, slot, object)

    def add_row(self, subject: str, slot: str, obj: str) -> None:
        self.rows.append((subject, slot, obj))

    def add_prefix(self, px: str, uri: str) -> None:
        self.prefix_uris.setdefault(px, uri)

    def build_for_prefixes(self, prefixes: set[str]) -> None:
        """Populate ``by_name`` keeping only rows whose subject uses one of
        the given local prefixes."""
        self.by_name.clear()
        prefs_with_colon = tuple(f"{p}:" for p in prefixes)
        for subject, slot, obj in self.rows:
            local: str | None = None
            for px in prefs_with_colon:
                if subject.startswith(px):
                    local = subject[len(px):]
                    break
            if local is None:
                continue
            slot_map = self.by_name.setdefault(local, {})
            entries = slot_map.setdefault(slot, [])
            if obj not in entries:
                entries.append(obj)

    def used_prefixes_for(self, name: str) -> set[str]:
        out: set[str] = set()
        for curies in self.by_name.get(name, {}).values():
            for c in curies:
                if ":" in c:
                    out.add(c.split(":", 1)[0])
        return out


def load_mappings(mappings_dir: Path) -> MappingIndex:
    """Load every ``*.sssom.tsv`` under ``mappings_dir`` into one index."""
    idx = MappingIndex()
    for tsv in sorted(mappings_dir.glob("*.sssom.tsv")):
        meta = _parse_sssom_metadata(tsv)
        curie_map = meta.get("curie_map") or {}
        if isinstance(curie_map, dict):
            for px, uri in curie_map.items():
                if px in _BUILTIN_PREFIXES:
                    continue
                idx.add_prefix(px, uri)

        header, rows = _parse_sssom_rows(tsv)
        if not header:
            continue
        col = {name: i for i, name in enumerate(header)}
        try:
            si = col["subject_id"]
            pi = col["predicate_id"]
            oi = col["object_id"]
        except KeyError as missing:
            print(
                f"WARN: {tsv.name} missing required column "
                f"{missing.args[0]!r}; skipping file",
                file=sys.stderr,
            )
            continue
        for row in rows:
            if len(row) <= max(si, pi, oi):
                continue
            subject = row[si].strip()
            predicate = row[pi].strip()
            obj = row[oi].strip()
            slot = SSSOM_PREDICATE_TO_LINKML_SLOT.get(predicate)
            if slot is None or not subject or not obj:
                continue
            idx.add_row(subject, slot, obj)
    return idx


# ---------------------------------------------------------------------------
# Subject-prefix discovery
# ---------------------------------------------------------------------------


def discover_subject_prefixes(data: CommentedMap) -> set[str]:
    """Return the set of CURIE prefixes that identify the schema itself.

    Includes ``default_prefix`` and ``name`` (the LinkML schema name is
    commonly registered as a prefix in the schema's own ``prefixes`` block).
    """
    out: set[str] = set()
    for key in ("default_prefix", "name"):
        v = data.get(key)
        if isinstance(v, str) and v:
            out.add(v)
    return out


# ---------------------------------------------------------------------------
# YAML overlay
# ---------------------------------------------------------------------------


def _insert_mapping_slot(
    body: CommentedMap,
    slot: str,
    curies: list[str],
) -> None:
    """Place ``slot`` at its canonical position within ``body``.

    If ``slot`` already exists, its value is replaced in place. Otherwise it
    is inserted just after the latest preceding mapping slot already in
    ``body``; failing that, before the next succeeding mapping slot; failing
    that, before the first post-mapping anchor; failing that, appended.
    """
    seq = CommentedSeq(curies)

    if slot in body:
        body[slot] = seq
        return

    keys = list(body.keys())
    slot_idx = _MAPPING_SLOT_ORDER.index(slot)

    insert_pos: int | None = None
    # 1. after latest preceding mapping slot
    for s in _MAPPING_SLOT_ORDER[:slot_idx]:
        if s in body:
            insert_pos = keys.index(s) + 1
    # 2. before next mapping slot
    if insert_pos is None:
        for s in _MAPPING_SLOT_ORDER[slot_idx + 1:]:
            if s in body:
                insert_pos = keys.index(s)
                break
    # 3. before first post-mapping anchor
    if insert_pos is None:
        for k in _POST_MAPPING_ANCHORS:
            if k in body:
                insert_pos = keys.index(k)
                break
    # 4. append
    if insert_pos is None:
        body[slot] = seq
        return

    body.insert(insert_pos, slot, seq)


def _merge_mappings(
    body: CommentedMap,
    slot_map: dict[str, list[str]],
    *,
    is_permissible_value: bool = False,
) -> tuple[bool, int]:
    """Merge ``slot_map`` into ``body``. Returns ``(touched, links_added)``.

    When ``is_permissible_value`` is True the LinkML ``meaning`` slot
    (singleton CURIE) is preferred for the first ``exact_mappings`` entry,
    per the LinkML PermissibleValue model. Any additional exact mappings
    still land in ``exact_mappings`` so no information is lost.
    """
    touched = False
    links_added = 0
    for slot in _MAPPING_SLOT_ORDER:
        curies = slot_map.get(slot)
        if not curies:
            continue

        # Special-case: PV + exact_mappings -> populate `meaning` first.
        if is_permissible_value and slot == "exact_mappings":
            remaining = list(curies)
            current_meaning = body.get("meaning")
            if not current_meaning:
                first = remaining.pop(0)
                _set_pv_meaning(body, first)
                links_added += 1
                touched = True
            else:
                # Don't re-add the value already used as `meaning`.
                remaining = [c for c in remaining if c != current_meaning]
            if not remaining:
                continue
            curies = remaining  # fall through to normal list merge

        existing = body.get(slot)
        if existing is None:
            _insert_mapping_slot(body, slot, list(curies))
            links_added += len(curies)
            touched = True
        else:
            new_list = list(existing)
            added_here = 0
            for c in curies:
                if c not in new_list:
                    new_list.append(c)
                    added_here += 1
            if added_here:
                body[slot] = CommentedSeq(new_list)
                links_added += added_here
                touched = True
    return touched, links_added


# Anchors used to position the singleton `meaning` slot inside a PV body
# (LinkML conventional order: description, meaning, title, aliases, ...).
_PV_PRE_MEANING_KEYS = ("meaning", "description", "title")
_PV_POST_MEANING_KEYS = (
    "title", "aliases", "annotations", "comments", "in_subset",
    "exact_mappings", "close_mappings", "broad_mappings",
    "narrow_mappings", "related_mappings",
)


def _set_pv_meaning(body: CommentedMap, curie: str) -> None:
    """Insert/replace the ``meaning`` slot on a permissible-value body."""
    if "meaning" in body:
        body["meaning"] = curie
        return
    keys = list(body.keys())
    insert_pos: int | None = None
    # Place right after `description` if present, else before the first
    # post-meaning anchor, else append.
    if "description" in body:
        insert_pos = keys.index("description") + 1
    else:
        for k in _PV_POST_MEANING_KEYS:
            if k in body:
                insert_pos = keys.index(k)
                break
    if insert_pos is None:
        body["meaning"] = curie
    else:
        body.insert(insert_pos, "meaning", curie)


def _ensure_prefixes(
    data: CommentedMap,
    needed: set[str],
    prefix_uris: dict[str, str],
    own_prefixes: set[str],
) -> bool:
    """Add referenced prefixes to ``data['prefixes']``. Returns changed flag."""
    changed = False
    prefixes = data.get("prefixes")
    if not isinstance(prefixes, dict):
        prefixes = CommentedMap()
        data["prefixes"] = prefixes
    for px in sorted(needed):
        if px in _BUILTIN_PREFIXES or px in own_prefixes:
            continue
        if px in prefixes:
            continue
        uri = prefix_uris.get(px)
        if uri is None:
            print(
                f"WARN: prefix {px!r} referenced by a mapping but no URI "
                f"found in any sssom curie_map; declare it manually.",
                file=sys.stderr,
            )
            continue
        prefixes[px] = uri
        changed = True
    return changed


# ---------------------------------------------------------------------------
# Whole-file overlay
# ---------------------------------------------------------------------------


def _make_yaml() -> YAML:
    y = YAML(typ="rt")
    y.preserve_quotes = True
    y.width = 4096
    y.indent(mapping=2, sequence=4, offset=2)
    return y


def overlay_file(
    schema_path: Path,
    mappings: MappingIndex,
    extra_subject_prefixes: set[str],
) -> tuple[int, int]:
    """Overlay mappings onto one schema YAML in place.

    Returns ``(elements_updated, links_added)``. The file is rewritten only
    when at least one element was modified or a new prefix was declared.
    """
    y = _make_yaml()
    with open(schema_path, "r", encoding="utf-8") as fh:
        data = y.load(fh)
    if data is None:
        return 0, 0

    subject_prefixes = discover_subject_prefixes(data) | extra_subject_prefixes
    if not subject_prefixes:
        print(
            f"WARN: {schema_path.name} has no default_prefix/name and no "
            "--subject-prefix was supplied; skipping.",
            file=sys.stderr,
        )
        return 0, 0
    mappings.build_for_prefixes(subject_prefixes)
    if not mappings.by_name:
        return 0, 0

    own = subject_prefixes
    elements_updated = 0
    links_added = 0
    used_prefixes: set[str] = set()

    for collection_key in ("classes", "slots", "enums", "types"):
        collection = data.get(collection_key)
        if not isinstance(collection, dict):
            continue
        for name, body in collection.items():
            if not isinstance(body, CommentedMap):
                continue
            slot_map = mappings.by_name.get(name)
            if slot_map:
                touched, n_added = _merge_mappings(body, slot_map)
                if touched:
                    elements_updated += 1
                    links_added += n_added
                    used_prefixes |= mappings.used_prefixes_for(name)

            # Recurse into permissible_values for enum bodies.
            if collection_key == "enums":
                pvs = body.get("permissible_values")
                if isinstance(pvs, dict):
                    for pv_name, pv_body in pvs.items():
                        if not isinstance(pv_body, CommentedMap):
                            continue
                        pv_slot_map = mappings.by_name.get(pv_name)
                        if not pv_slot_map:
                            continue
                        touched, n_added = _merge_mappings(
                            pv_body, pv_slot_map, is_permissible_value=True,
                        )
                        if touched:
                            elements_updated += 1
                            links_added += n_added
                            used_prefixes |= mappings.used_prefixes_for(pv_name)

    prefixes_changed = _ensure_prefixes(
        data, used_prefixes, mappings.prefix_uris, own
    )

    if elements_updated or prefixes_changed:
        with open(schema_path, "w", encoding="utf-8") as fh:
            y.dump(data, fh)
    return elements_updated, links_added


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    src = p.add_mutually_exclusive_group()
    src.add_argument(
        "--schema-dir", type=Path,
        help="directory containing LinkML schema YAML files",
    )
    src.add_argument(
        "--schema", type=Path,
        help="single LinkML schema YAML file",
    )
    p.add_argument(
        "--mappings-dir", type=Path, required=True,
        help="directory containing *.sssom.tsv mapping files",
    )
    p.add_argument(
        "--subject-prefix", action="append", default=[],
        help="extra CURIE prefix (without colon) to treat as a subject-side "
             "match in addition to those discovered from each schema "
             "(repeatable)",
    )
    args = p.parse_args(argv)

    if not args.schema_dir and not args.schema:
        print("ERROR: one of --schema-dir or --schema is required",
              file=sys.stderr)
        return 1
    if not args.mappings_dir.is_dir():
        print(f"ERROR: mappings-dir {args.mappings_dir} is not a directory",
              file=sys.stderr)
        return 1

    if args.schema:
        if not args.schema.is_file():
            print(f"ERROR: schema {args.schema} is not a file", file=sys.stderr)
            return 1
        schemas = [args.schema]
    else:
        if not args.schema_dir.is_dir():
            print(f"ERROR: schema-dir {args.schema_dir} is not a directory",
                  file=sys.stderr)
            return 1
        schemas = sorted(args.schema_dir.glob("*.yaml"))
        modules_dir = args.schema_dir / "modules"
        if modules_dir.is_dir():
            schemas = sorted(schemas + list(modules_dir.glob("*.yaml")))
        extensions_dir = args.schema_dir / "extensions"
        if extensions_dir.is_dir():
            # Extension schemas can live at any depth (e.g. legal/eu/gdpr.yaml)
            schemas = sorted(schemas + list(extensions_dir.rglob("*.yaml")))
        if not schemas:
            print(f"No YAML schemas in {args.schema_dir}", file=sys.stderr)
            return 1

    mappings = load_mappings(args.mappings_dir)
    if not mappings.rows:
        print(f"No mapping rows loaded from {args.mappings_dir}",
              file=sys.stderr)
        return 0

    extra_prefixes = {px.rstrip(":") for px in args.subject_prefix if px}

    files_changed = 0
    total_elements = 0
    total_links = 0
    for path in schemas:
        elements, links = overlay_file(path, mappings, extra_prefixes)
        if elements:
            files_changed += 1
            total_elements += elements
            total_links += links
            print(f"  {path.name}: +{links} links across {elements} elements")

    if total_links:
        print(
            f"\nOverlay complete: {total_links} new mappings applied to "
            f"{total_elements} elements across {files_changed} files"
        )
    else:
        print(
            "\nOverlay complete: schemas already in sync with SSSOM files "
            "- no changes needed"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
