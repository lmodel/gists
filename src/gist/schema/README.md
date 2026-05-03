# GIST LinkML Schema Project

**Status**:  **Operational** | **Tests**: 228/228 passing | **Version**: 14.1.0

## Overview

This project provides a comprehensive **LinkML schema representation** of **GIST**.

The project converts the GIST OWL/RDF ontology into a modular, validated LinkML schema with:
-  Comprehensive test coverage (228 unit tests)
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
| Unit Tests |  228 passing | Schema, data, SHACL, OWL conversion, artifacts |
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
# Run all 228 tests
just test

# Run test suites individually
just test-schema        # Schema validation (31 tests)
just test-shacl         # SHACL validation (18 tests)
just test-artifacts     # Code generation (14 tests)
just test-data          # Data validation (11 tests)
just test-owl           # OWL conversion (154 tests)

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
├── gist.yaml                        # Main schema (3 imports, all prefixes)
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
- **Semantic URIs**: All classes and properties mapped to gist_upstream namespace
- **RDF/OWL Support**: Exportable to OWL/Turtle format

## Test Coverage

### Statistics: 228 Tests Passing 

#### By Type
| Type | Count | Details |
|------|-------|---------|
| Schema Validation | 31 | Structure, elements, consistency, ontology alignment |
| Generated Artifacts | 14 | Python, JSON Schema, YAML validity |
| SHACL Validation | 18 | Semantic Arts shapes, RDF compliance |
| Data Validation | 11 | Valid/invalid YAML examples |
| OWL Conversion | 154 | Conversion logic, utilities, integration |
| **Total** | **228** | **All passing**  |

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
.venv/bin/python scripts/owl_to_linkml.py
```

Regenerates schema YAML from OWL source files.


## Known Issues & Limitations

### Resolved
-  Prefix naming conflicts (hyphens  -> underscores)
-  Missing namespaces in generated code
-  Data validation test module integration

### Current Limitations
1. OWL-to-LinkML conversion doesn't support all complex OWL restrictions
2. Enum values with special characters require name conversion (e.g., `ld+json`  -> `LD_PLUS_JSON`)
3. Some SHACL constraints may not validate deeply nested polymorphic data

### Working Well
-  Schema validation and linting
-  Python datamodel generation
-  SHACL shape compliance
-  Data validation
-  Documentation generation
-  Multi-format code generation

