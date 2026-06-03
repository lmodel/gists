## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Generate LinkML schema YAMLs from the upstream GIST OWL/Turtle ontology files.
# Reads upstream/gist14.1.0_webDownload/ontologies/turtle/*.ttl and writes to src/gist/schema/.
# Build order: `gen-linkml` -> `apply-sssom-overlay` -> `gen-project`.
[group('model development')]
gen-linkml:
  uv run python scripts/gist_to_linkml.py

# Apply curated SSSOM mapping TSVs to the generated LinkML schema YAMLs.
# Merges SKOS exact/close/broad/narrow/related matches into the matching
# class / enum / type bodies and declares any referenced object-side prefixes.
# Idempotent: re-running on a clean tree produces no further changes.
[group('model development')]
apply-sssom-overlay: gen-linkml
  uv run python scripts/apply_sssom_overlay.py \
    --schema-dir src/gist/schema \
    --mappings-dir src/gist/mappings

# Verify the mappings were applied correctly to LinkML files.
[group('model development')]
verify-mappings: apply-sssom-overlay
  uv run python scripts/verify_mappings.py
