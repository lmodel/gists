"""Verify that the LinkML schemas reflect the SSSOM mapping TSV files.

The SSSOM TSV files under ``src/<project>/mappings/`` are the
authoritative source of cross-vocabulary mappings. This script reads
them and confirms that the corresponding ``exact_mappings`` /
``close_mappings`` / ``broad_mappings`` / ``narrow_mappings`` /
``related_mappings`` fields are present on the matching elements in
the LinkML schemas under ``src/<project>/schema/`` (recursively, so
module YAMLs are included).

This is a *verifier* (read-only) so that the hand-curated YAML
comments and formatting in the schemas are never disturbed. If a
mapping is in the TSV but missing from the schema (or vice versa) the
script prints a diff and exits non-zero.

Schemas are auto-discovered: every ``*.yaml`` under ``--schema-dir``
is loaded, and the subject prefix from each SSSOM row is matched
against each schema's ``default_prefix``. An element name found in
*any* matching schema satisfies the row.

Run via ``just verify-mappings`` (or directly:
``python scripts/verify_mappings.py``).
"""

from __future__ import annotations

import argparse
import csv
import io
import sys
from collections import defaultdict
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCHEMA_DIR = REPO_ROOT / "src" / "gists" / "schema"
DEFAULT_MAPPINGS_DIR = REPO_ROOT / "src" / "gists" / "mappings"

PREDICATE_TO_FIELD: dict[str, str] = {
    "skos:exactMatch": "exact_mappings",
    "skos:closeMatch": "close_mappings",
    "skos:broadMatch": "broad_mappings",
    "skos:narrowMatch": "narrow_mappings",
    "skos:relatedMatch": "related_mappings",
}

# Predicates that appear in upstream SSSOM TSVs but do not correspond to
# any LinkML mapping slot; silently skipped to match apply_sssom_overlay.
IGNORED_PREDICATES: frozenset[str] = frozenset(
    {"skos:broader", "skos:narrower", "rdf:type", "owl:equivalentClass"}
)

ELEMENT_SECTIONS = ("classes", "slots", "enums", "types")


def parse_sssom_tsv(path: Path) -> list[dict[str, str]]:
    """Return the SSSOM data rows (header comment lines and blanks are skipped)."""
    text_lines = [
        ln
        for ln in path.read_text().splitlines()
        if ln.strip() and not ln.lstrip().startswith("#")
    ]
    reader = csv.DictReader(io.StringIO("\n".join(text_lines)), delimiter="\t")
    return [row for row in reader if row.get("subject_id")]


def expected_mappings(rows: list[dict[str, str]]) -> dict[str, dict[str, set[str]]]:
    """``{local_name: {field: {object_curie, ...}}}`` derived from TSV."""
    expected: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    for row in rows:
        predicate = row["predicate_id"]
        if predicate in IGNORED_PREDICATES:
            continue
        if predicate not in PREDICATE_TO_FIELD:
            print(
                f"WARNING: unsupported predicate {predicate!r} (subject={row['subject_id']})",
                file=sys.stderr,
            )
            continue
        local = row["subject_id"].split(":", 1)[-1]
        field = PREDICATE_TO_FIELD[predicate]
        expected[local][field].add(row["object_id"])
    return expected


def find_element(schema: dict, name: str) -> tuple[str, dict] | None:
    """Locate an element by local name.

    Searches the top-level ``classes``/``slots``/``enums``/``types``
    sections first, then inline ``attributes`` defined on a class
    (which LinkML treats as locally-scoped slots). Returns
    ``(location, element)`` or ``None`` if not found.
    """
    for section in ELEMENT_SECTIONS:
        element = (schema.get(section) or {}).get(name)
        if element is not None:
            return section, element
    for class_name, cls in (schema.get("classes") or {}).items():
        attrs = (cls or {}).get("attributes") or {}
        if name in attrs:
            return f"classes.{class_name}.attributes", attrs[name]
    return None


def element_mappings(element: dict) -> dict[str, set[str]]:
    """Read mapping fields off a schema element."""
    return {
        field: set(element.get(field) or [])
        for field in PREDICATE_TO_FIELD.values()
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--schema-dir",
        type=Path,
        default=DEFAULT_SCHEMA_DIR,
        help=f"Directory of LinkML schemas (recursively scanned). Default: {DEFAULT_SCHEMA_DIR}",
    )
    parser.add_argument(
        "--mappings-dir",
        type=Path,
        default=DEFAULT_MAPPINGS_DIR,
        help=f"Directory of *.sssom.tsv files. Default: {DEFAULT_MAPPINGS_DIR}",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Also fail when the schema has mappings that the TSV does not declare.",
    )
    args = parser.parse_args(argv)

    if not args.schema_dir.is_dir():
        print(f"ERROR: schema dir not found: {args.schema_dir}", file=sys.stderr)
        return 2
    if not args.mappings_dir.is_dir():
        print(f"ERROR: mappings dir not found: {args.mappings_dir}", file=sys.stderr)
        return 2

    # Load every schema yaml under schema-dir (recursively so per-extension
    # sub-schemas with their own default_prefix - e.g. ``extensions/loc.yaml``
    # with default_prefix ``loc`` - are discoverable).
    schemas_by_prefix: dict[str, list[tuple[Path, dict]]] = defaultdict(list)
    schema_files: list[Path] = sorted(args.schema_dir.rglob("*.yaml"))
    for path in schema_files:
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError as exc:
            print(f"  WARN: failed to parse {path}: {exc}", file=sys.stderr)
            continue
        if not isinstance(doc, dict):
            continue
        prefix = doc.get("default_prefix")
        if not prefix:
            continue
        schemas_by_prefix[prefix].append((path, doc))

    if not schemas_by_prefix:
        print(f"ERROR: no schemas with default_prefix found under {args.schema_dir}", file=sys.stderr)
        return 2

    print(
        f"Loaded {sum(len(v) for v in schemas_by_prefix.values())} schema(s) "
        f"across prefixes: {sorted(schemas_by_prefix)}"
    )

    overall_missing: list[str] = []
    overall_extra: list[str] = []
    overall_unknown: list[str] = []
    total_rows = 0

    for tsv in sorted(args.mappings_dir.glob("*.sssom.tsv")):
        rows = parse_sssom_tsv(tsv)
        total_rows += len(rows)
        print(f"== {tsv.name} ({len(rows)} mappings) ==")

        by_prefix: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in rows:
            prefix = row["subject_id"].split(":", 1)[0]
            by_prefix[prefix].append(row)

        file_problems = 0
        for prefix, prefix_rows in by_prefix.items():
            candidate_schemas = schemas_by_prefix.get(prefix)
            if not candidate_schemas:
                msg = f"{tsv.name}: unknown subject prefix {prefix!r} (no schema has default_prefix: {prefix})"
                overall_unknown.append(msg)
                print(f"  UNKNOWN-PREFIX: {msg}")
                file_problems += len(prefix_rows)
                continue

            expected = expected_mappings(prefix_rows)
            for name, fields in sorted(expected.items()):
                located: list[tuple[Path, str, dict]] = []
                for schema_path, schema_doc in candidate_schemas:
                    found = find_element(schema_doc, name)
                    if found is not None:
                        section, element = found
                        located.append((schema_path, section, element))
                if not located:
                    schema_names = ", ".join(p.name for p, _ in candidate_schemas)
                    msg = (
                        f"{tsv.name}: element {prefix}:{name!r} not found in any "
                        f"schema with default_prefix {prefix!r} ({schema_names})"
                    )
                    overall_unknown.append(msg)
                    print(f"  MISSING-ELEMENT: {msg}")
                    file_problems += 1
                    continue
                for schema_path, section, element in located:
                    actual = element_mappings(element)
                    for field, exp_set in fields.items():
                        act_set = actual.get(field, set())
                        missing = exp_set - act_set
                        extra = act_set - exp_set
                        if missing:
                            msg = (
                                f"{schema_path.name}: {section}.{name}.{field} "
                                f"missing: {sorted(missing)}"
                            )
                            overall_missing.append(msg)
                            print(f"  MISSING: {msg}")
                            file_problems += 1
                        if extra and args.strict:
                            msg = (
                                f"{schema_path.name}: {section}.{name}.{field} "
                                f"extra (not in TSV): {sorted(extra)}"
                            )
                            overall_extra.append(msg)
                            print(f"  EXTRA: {msg}")
                            file_problems += 1
        if file_problems == 0:
            print(f"  OK")

    print()
    print(
        f"Summary: rows={total_rows} missing={len(overall_missing)} "
        f"extra={len(overall_extra)} unknown={len(overall_unknown)}"
    )
    if overall_missing or overall_unknown:
        print(
            "\nApply the missing mappings to the schema YAML, "
            "or remove the rows from the SSSOM TSV.",
            file=sys.stderr,
        )
        return 1
    if overall_extra and args.strict:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
