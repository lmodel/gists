# About gist

Gist - LinkML Schema

**Status**:  **Operational** | **Tests**: 236/237 passing | **Version**: 14.1.0 | **Upstream OWL parity**: taxonomic skeleton ✅, DL axioms ❌ (see Full-Circle Fidelity)

The project converts the GIST OWL/RDF ontology into a modular, validated LinkML schema with:
-  Comprehensive test coverage (236 unit tests)
-  Auto-generated Python datamodel
-  SHACL shape validation
-  Multi-format code generation (JSON Schema, OWL, TypeScript, Java)
-  Semantic Arts validation integration

**Schema License**: CC-BY-4.0
**Project License**: Apache-2.0
**Documentation**: [https://lmodel.github.io/gist](https://lmodel.github.io/gist)

## Project Status

| Component | Status | Details |
|-----------|--------|---------|
| Schema Structure |  Complete | 3 modular schemas: core, media-types, prefix-declarations |
| Python Datamodel |  Generated | Auto-generated from LinkML, imports successfully |
| Unit Tests |  236 passing, 1 skipped | Schema, data, SHACL, OWL conversion, artifacts |
| Data Validation |  Working | Valid (4) and invalid (3) test examples included |
| Documentation |  Generated | Markdown docs from schema auto-generated |
| Code Generation |  All formats | Python, JSON Schema, OWL/TTL, TypeScript, Java |

## Quick Start

### Installation

```bash
# Install dependencies using uv (recommended)
just install

# Or manually
uv sync --group dev
```

### Generate Project Artifacts

```bash
# Generate all artifacts
just gen-project

# Just Python datamodel
just gen-python

# Just documentation
just gen-doc
```

### Run Tests

```bash
# Run all 236 tests
just test

# Run test suites individually
just test-schema        # Schema validation (31 tests)
just test-shacl         # SHACL validation (18 tests)
just test-artifacts     # Code generation (13 tests, 1 skipped)
just test-data          # Data validation (11 tests)
just test-owl           # OWL conversion (163 tests)

# With coverage
just test-coverage

# Watch mode (auto-rerun)
just test-watch
```

### Validate Schema

```bash
# Lint for structural errors
just lint

# Run all validation gates
just test-all
```

## Schema Organization

This folder contains the LinkML schema YAML files:

```
.
├── gist.yaml                 # Main schema (3 imports, all prefixes)
├── gist_core.yaml                  # Core classes and properties
├── gist_media_types.yaml           # IANA media type instances
├── gist_prefix_declarations.yaml   # SHACL prefix bindings
├── gist_rdfs_annotations.yaml      # RDFS enrichment
├── gist_sub_class_assertions.yaml  # OWL RL support
└── README.md                        # This file
```

## Modular Structure

The main schema (`gist.yaml`) imports three specialized modules:

1. **gist_core.yaml** - Core ontology
   - Classes: Thing, Entity, Activity, Event, etc.
   - Properties: is_a, has_aspect, is_produced_by, etc.
   - Enums: AspectInstance

2. **gist_media_types.yaml** - IANA Media Types
   - MediaTypeInstance enum with 20+ types (JSON, XML, RDF, etc.)
   - Mappings to IANA media type URIs

3. **gist_prefix_declarations.yaml** - SHACL Bindings
   - PrefixDeclarationInstance enum
   - Namespace bindings for semantic web

## Ontology Alignment

- **Exact Mappings**: Schema.org, Wikidata, NCIT
- **Semantic URIs**: All classes and properties mapped to gist  namespace
- **RDF/OWL Support**: Exportable to OWL/Turtle format via `gen-owl`

### Full-Circle Fidelity (gist 14.1.0 upstream OWL vs `gen-owl` output)

Schema enrichments were derived from the upstream TTL files so that `gen-owl` reproduces the corresponding OWL axioms. Counts are based on the full upstream TTL corpus and a fresh `gen-owl` run (LinkML 1.11.0).

**Headline assessment**: the generated [project/owl/gist.owl.ttl](../project/owl/gist.owl.ttl) (single file, ~133 KB, 2,214 lines) reproduces the **taxonomic skeleton** of upstream gist 14.1.0 (5 files, ~270 KB, 6,149 lines) — class/property hierarchy, ranges, single inheritance, SKOS definitions, and `skos:exactMatch` bridges to the source `gist:` IRIs. It is a **lossy projection** for reasoning purposes: 95% of `owl:Restriction` blocks (109 in upstream gistCore → 6 in the generated file, all on `GistThing.name`/`description`), all 20 `owl:disjointWith` axioms, all 147 `skos:example` strings, and the 216 `rdfs:isDefinedBy` back-pointers are absent. The 45 `owl:equivalentClass` intersection axioms (e.g. `Account ≡ Agreement ⊓ ∃hasMagnitude.∃hasAspect=balance`) survive only as prose inside `skos:editorialNote` and are invisible to DL reasoners. See the structural-gaps and gen-owl-gaps tables below.

**Namespace note**: gen-owl emits properties in the `gist_linkml:` namespace with snake_case names (e.g. `gist_linkml:conversion_factor`), bridged to the upstream `gist:` camelCase IRIs via `skos:exactMatch` (97 triples). 106 of 120 properties are affected (the 14 single-word properties share the same local name but still differ in namespace). Domain/range triples in the tables below are in the correct structure but attached to different property IRIs than the upstream. See Gap 9 in [ISSUE.md](../ISSUE.md).

**Companion artifacts not regenerated**: the upstream distribution ships two supplementary TTL files alongside `gistCore14.1.0.ttl` — `gistRdfsAnnotations14.1.0.ttl` (definitions/examples/notes flattened into `rdfs:comment` for tools that don't read SKOS) and `gistSubClassAssertions14.1.0.ttl` (explicit subclass closure to support OWL RL reasoners). Neither is produced by `gen-project`. The single-file gen-owl output addresses the OWL DL consumer only.

#### Exact parity

| Axiom | Upstream | gen-owl | Notes |
|-------|----------|---------|-------|
| `owl:ObjectProperty` | 66 | 66 | All 66 object properties correctly classified (via `implements: [owl:ObjectProperty]` workaround — Gap 8) |
| `owl:DatatypeProperty` | 50 | 50 | All 50 datatype properties (via `implements: [owl:DatatypeProperty]`) |
| `owl:AnnotationProperty` | 4 | 4 | All 4 gist-namespace annotation properties (via `implements: [owl:AnnotationProperty]`); 7 upstream skos:* redeclarations not replicated |
| `rdfs:seeAlso` | 4 | 4 | `Magnitude`, `hasAccuracy`, `conversionFactor`, `MediaType` |
| `owl:SymmetricProperty` | 1 | 1 | `isConnectedTo` |
| `owl:TransitiveProperty` | 5 | 5 | All 5 transitive properties |
| `rdfs:domain` | 27 | 27 | All `domain:` assertions emitted; different IRIs — see namespace note |
| `owl:inverseOf` | 0 | 0 | Upstream does not declare `owl:inverseOf` between named properties; all 18 upstream `owl:inverseOf` are anonymous (inside class restrictions, not on named pairs) |

#### Approximate parity (within ±15%, expected from namespace translation and LinkML mediating classes)

| Axiom | Upstream | gen-owl | Delta | Notes |
|-------|----------|---------|-------|-------|
| `rdfs:subPropertyOf` | 40 | 38 | −5% | |
| `skos:definition` (from `description:`) | 228 | 236 | +3% | |
| `rdfs:range` | 65 | 73 | +12% | gen-owl adds ranges from `any_of:` and type inference |

#### Present but not fidelity-matched

| Axiom | Upstream | gen-owl | Explanation |
|-------|----------|---------|-------------|
| `skos:altLabel` | 1 | 217 | Upstream: 1 (`ElectronicAddress`). gen-owl emits `skos:altLabel` for all `aliases:` entries across the schema (many schema-level aliases added for usability) |
| `skos:exactMatch` | 0 | 97 | gen-owl bridges `gist:` ↔ `gist:` via `exact_mappings:` / `slot_uri:` — not in upstream |

#### Schema enrichments added to achieve parity

| Enrichment | Source in upstream OWL | Schema field |
|-----------|------------------------|--------------|
| `implements: [owl:ObjectProperty]` on 66 slots | `owl:ObjectProperty` | `implements:` ✅ re-emitted (workaround for Gap 8) |
| `implements: [owl:DatatypeProperty]` on 50 slots | `owl:DatatypeProperty` | `implements:` ✅ re-emitted |
| `implements: [owl:AnnotationProperty]` on 4 slots | `owl:AnnotationProperty` | `implements:` ✅ re-emitted |
| `maximum_cardinality: 1` on 9 slots | `owl:FunctionalProperty` | `maximum_cardinality:` (semantically equivalent; not re-emitted as `owl:FunctionalProperty` — Gap 3) |
| `see_also:` on 4 entities | `rdfs:seeAlso` triples | `see_also:` ✅ re-emitted |
| `annotations: {owl_functional: true}` on 9 slots | `owl:FunctionalProperty` | `annotations:` (documentation only — Gap 3) |
| `annotations: {owl_inverse_functional: true}` on `is_identified_by` | `owl:InverseFunctionalProperty` | `annotations:` (workaround — Gap 3) |
| `notes:` on 8 `AspectInstance` enum values + `Landmark` + `prevents` | `skos:editorialNote` | `notes:` |
| `deprecated: 'true'` + `deprecated_element_has_exact_replacement:` on 5 elements | `owl:deprecated true` + `gist:isSupersededBy` | `deprecated:` (not re-emitted — Gap 2) |
| `disjoint_with:` on 62 class pairs + 1 slot pair | `owl:disjointWith` | `disjoint_with:` (not re-emitted — Gap 1) |
| `domain:` on 27 slots | `rdfs:domain` | `domain:` ✅ re-emitted |
| `range:` on 120 slots | `rdfs:range` | `range:` ✅ re-emitted |
| `aliases:` on `ElectronicAddress` (`Virtual Address`) | `skos:altLabel` | `aliases:` ✅ re-emitted |
| `exact_mappings: [gist:prohibits]` on `prevents` | `owl:equivalentProperty` | `exact_mappings:` (emits `skos:exactMatch` — Gap 7) |

#### Not representable in LinkML (structural gaps)

The following upstream OWL constructs have no LinkML metamodel equivalent and
cannot be captured in the schema at all:

| OWL construct | Upstream count | Notes |
|---------------|---------------|-------|
| `owl:Restriction` blocks (any kind) | 109 | Aggregate of all property restrictions in gistCore; only 6 cardinality restrictions survive in gen-owl output (on `GistThing.name`/`description`) |
| `owl:equivalentClass` with OWL expressions | 45 | Complex restrictions (existential, intersection, union) on class definitions; preserved only as prose in `skos:editorialNote` |
| `owl:hasValue` in class restrictions | 10 | e.g. `Account owl:hasValue gistd:_Aspect_financial_balance` |
| `owl:allValuesFrom` in class restrictions | 4 | Universal quantifier on property |
| `owl:cardinality` in class restrictions | 9 | Exact cardinality on class-scoped property |
| `owl:inverseOf` inside class restrictions | 18 | Anonymous inverses used in `equivalentClass` intersections; reduced to `∃^propertyName` notation in editorial text |
| `rdfs:domain` as union class | 14 | `exponentOf*` domain is `union[UnitGroup, UnitOfMeasure]`; LinkML `domain:` accepts only a single class |
| `rdfs:isDefinedBy` | 216 | No LinkML metamodel slot; not emitted (Gap 6) |
| `owl:versionIRI`, `skos:historyNote` on ontology header | 1+1 | Ontology header carries only `pav:version`; release history (back to 11.0.0) is lost |
| Reference-data instances (`gistd:_Aspect_*`) typed as class members | 8 | Upstream: `gistd:_Aspect_altitude a gist:Aspect` (named individual usable inside `owl:hasValue`). gen-owl punning emits `a owl:Class ; rdfs:subClassOf gist_linkml:AspectInstance`. The original semantics required for `hasValue` restrictions are lost. |

Gaps where the schema holds information but gen-owl does not re-emit the
corresponding OWL axioms are fully documented in [ISSUE.md](../ISSUE.md).

#### Reasoning impact

A DL reasoner over the generated [project/owl/gist.owl.ttl](../project/owl/gist.owl.ttl) derives almost none of the entailments a reasoner over the upstream [gistCore14.1.0.ttl](../upstream/gist14.1.0_webDownload/ontologies/turtle/gistCore14.1.0.ttl) would: the restriction-bearing equivalent-class axioms and the 20 disjointness axioms — the two things that make gist a useful upper ontology for inference — are not present. The generated file is suitable as a **catalog / LinkML projection** and for SHACL-driven instance validation; it is not a substitute for the upstream OWL when DL inference is required.

## Test Coverage

### Statistics: 236 Tests Passing (1 Skipped)

#### By Type
| Type | Count | Details |
|------|-------|---------|
| Schema Validation | 31 | Structure, elements, consistency, ontology alignment |
| Generated Artifacts | 13 | Python, JSON Schema, YAML validity (1 skipped) |
| SHACL Validation | 18 | Semantic Arts shapes, RDF compliance |
| Data Validation | 11 | Valid/invalid YAML examples |
| OWL Conversion | 163 | Conversion logic, utilities, integration (+4 for `implements:` and `maximum_cardinality`) |
| **Total** | **236** | **All passing (1 skipped)**  |

#### Test Data Files

**Valid Examples** (in `../../tests/data/valid/`):
- `Account-basic.yaml` - Bank account with financial balance
- `Person-example.yaml` - Human individual record
- `Organization-sample.yaml` - Enterprise organization
- `System-example.yaml` - System arrangement

**Invalid Examples** (in `../../tests/data/invalid/`):
- `Account-invalid-id-type.yaml` - Wrong data type
- `Person-invalid-aspect.yaml` - Invalid enum value
- `Organization-minimal.yaml` - Missing required fields

## Development Workflow

### Making Schema Changes

```bash
# 1. Edit schema files in src/gist/schema/
# 2. Lint for errors
just lint

# 3. Regenerate artifacts
just gen-project

# 4. Run tests
just test-all

# 5. Commit
git add -A
git commit -m "Update schema: <description>"
```

### Adding Test Data

Create YAML files in `../../tests/data/valid/` or `../../tests/data/invalid/`:

```yaml
# ../../tests/data/valid/MyClass-description.yaml
id: "myclass-001"
title: "Example Instance"
description: "A valid example"
```

**Naming Convention**: `<ClassName>-<description>.yaml`

### Updating OWL Conversion

```bash
uv run python scripts/gen_linkml.py
```

Regenerates schema YAML from OWL source files.


## Known Issues & Limitations

### Resolved
-  Prefix naming conflicts (hyphens → underscores)
-  Missing namespaces in generated code
-  Data validation test module integration
-  Object property classification (Gap 8) — `implements:` workaround ensures gen-owl emits the correct OWL property type for all 120 slots, restoring full parity for `owl:ObjectProperty`, `owl:DatatypeProperty`, and `owl:AnnotationProperty` counts
-  FunctionalProperty semantics — captured as `maximum_cardinality: 1` (semantic equivalent; explicit `owl:FunctionalProperty` axiom emission still blocked by Gap 3)
-  `disjoint_with:` schema lint errors — now always emitted as a list per LinkML 1.9 array-form requirement

### gen-owl Round-Trip Gaps

The following `gen-owl` (LinkML 1.11.0) limitations prevent full OWL round-trip fidelity
with the upstream gist 14.1.0 ontology. Each gap is filed upstream; see [ISSUE.md](../ISSUE.md).

| # | Schema syntax | Expected OWL | Actual gen-owl output |
|---|--------------|--------------|----------------------|
| 1 | `disjoint_with:` | `owl:disjointWith` | Not emitted |
| 2 | `deprecated: 'true'` | `owl:deprecated true` | Not emitted |
| 3 | *(no metamodel slot)* | `owl:FunctionalProperty` / `owl:InverseFunctionalProperty` | No syntax available |
| 4 | `examples:` | `skos:example` | Not emitted |
| 5 | `description:` / `comments:` | `rdfs:comment` / `skos:scopeNote` | `skos:definition` / `skos:note` |
| 6 | *(no metamodel slot)* | `rdfs:isDefinedBy` | Not emitted |
| 7 | `exact_mappings:` | `owl:equivalentClass` | `skos:exactMatch` |
| 8 | `any_of: [{range: MyClass}]` | `owl:ObjectProperty` | `owl:DatatypeProperty` — ✅ resolved via `implements: [owl:ObjectProperty]` workaround |
| 9 | `slot_uri:` set to external namespace | Primary property IRI = `slot_uri` value | `slot_uri` emitted as `skos:exactMatch` target; slot name + `default_prefix` used as primary IRI — 106/120 properties affected |

### Other Limitations
- Enum values with special characters require name conversion (e.g., `ld+json` → `LD_PLUS_JSON`)
- Some SHACL constraints may not validate deeply nested polymorphic data

### Working Well
-  Schema validation and linting
-  Python datamodel generation
-  SHACL shape compliance
-  Data validation
-  Documentation generation
-  Multi-format code generation

