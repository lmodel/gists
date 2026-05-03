# gen-owl gaps: schema metadata not emitted as OWL axioms

**LinkML version:** 1.11.0  
**Discovered while:** comparing `gen-owl` output from the gistl schema against the upstream gist 14.1.0 OWL ontology to assess round-trip fidelity.

---

## Gap 1 — `disjoint_with:` not emitted as `owl:disjointWith`

### Description

The LinkML metamodel supports `disjoint_with` on both classes and slots
(`owl:propertyDisjointWith`). `gen-owl` silently ignores both.

The gistl schema has 62 class disjoint pairs and 1 slot disjoint pair.
None appear in the generated OWL.

### Minimal reproducer

```yaml
id: https://example.org/test
name: test
prefixes:
  linkml: https://w3id.org/linkml/
  test: https://example.org/test/
default_prefix: test
imports:
  - linkml:types

classes:
  Foo:
    disjoint_with:
      - Bar
  Bar: {}
```

Expected in output:
```turtle
test:Foo owl:disjointWith test:Bar .
```

Actual output: no `owl:disjointWith` triple emitted.

**Slot-level variant** (slot `disjoint_with` → `owl:propertyDisjointWith`):

```yaml
slots:
  has_giver:
    disjoint_with: has_recipient
```

Expected: `test:has_giver owl:propertyDisjointWith test:has_recipient .`  
Actual: nothing emitted.

### Suggested fix

In `owlgen.py`, visit `class_def.disjoint_with` and emit
`owl:disjointWith` for each entry. For slots, emit `owl:propertyDisjointWith`.
The values are slot/class names that need to be resolved via the schema's
`slot_uri` / `class_uri` (or constructed as local URIs).

---

## Gap 2 — `deprecated:` not emitted as `owl:deprecated`

### Description

LinkML's `deprecated` metamodel slot maps semantically to
`owl:deprecated true`. `gen-owl` does not emit `owl:deprecated` for any
element that has `deprecated: 'true'` in the schema.

The gistl schema has 5 deprecated elements (2 classes, 3 slots).
None produce `owl:deprecated true` in the generated OWL.

### Minimal reproducer

```yaml
classes:
  OldThing:
    deprecated: 'true'
    deprecated_element_has_exact_replacement: NewThing
  NewThing: {}
```

Expected:
```turtle
test:OldThing owl:deprecated true .
```

Actual: `test:OldThing` is defined as a normal `owl:Class` with no deprecation annotation.

### Suggested fix

In `owlgen.py`, when processing any `ClassDefinition`, `SlotDefinition`, or
`EnumDefinition` that has a truthy `deprecated` value, emit:
```turtle
<uri> owl:deprecated true .
```
Optionally also emit `rdfs:isDefinedBy` or a `skos:note` pointing to the
replacement element (`deprecated_element_has_exact_replacement` /
`deprecated_element_has_possible_replacement`).

---

## Gap 3 — No way to declare `owl:FunctionalProperty` / `owl:InverseFunctionalProperty`

### Description

There is no `functional` or `inverse_functional` slot in the LinkML
`SlotDefinition` metamodel class, so these OWL property characteristics
cannot be expressed in a schema. `gen-owl` therefore never emits
`owl:FunctionalProperty` or `owl:InverseFunctionalProperty`.

The gist ontology declares 9 functional properties and 1 inverse-functional
property. As a workaround, gistl uses freeform annotations
(`annotations: {owl_functional: true}` / `owl_inverse_functional: true`)
as documentation metadata, but `gen-owl` does not act on these.

### Minimal reproducer

There is no valid LinkML syntax to express this today. Attempting:

```yaml
slots:
  has_aspect:
    functional: true   # TypeError: SlotDefinition.__init__() got an unexpected keyword argument 'functional'
```

The annotation workaround that does **not** produce OWL output:

```yaml
slots:
  has_aspect:
    annotations:
      owl_functional: true   # gen-owl ignores this
```

### Suggested fix

**Option A** — Add `functional` and `inverse_functional` boolean slots to
`SlotDefinition` in the LinkML metamodel. In `owlgen.py`, emit
`owl:FunctionalProperty` / `owl:InverseFunctionalProperty` when set to `true`.

**Option B** — Treat the annotation keys `owl_functional` and
`owl_inverse_functional` (or a documented convention) as signals in `gen-owl`
and emit the corresponding OWL property type.

---

## Gap 4 — `examples:` not emitted as `skos:example`

### Description

LinkML's `examples` metamodel slot maps semantically to `skos:example`.
`gen-owl` does not emit `skos:example` for any element.

The gist ontology has 146 `skos:example` annotations. The gistl schema
carries these as `examples:` entries, but they are absent from the gen-owl
output.

### Minimal reproducer

```yaml
classes:
  Magnitude:
    description: The amount of a measurable characteristic.
    examples:
      - value: A model of car could have a wheelbase of 113.2 inches.
```

Expected:
```turtle
test:Magnitude skos:example "A model of car could have a wheelbase of 113.2 inches." .
```

Actual: no `skos:example` triple emitted.

### Suggested fix

In `owlgen.py`, when processing class/slot/type definitions, iterate
`element.examples` and emit one `skos:example` literal per `Example.value`.
The `skos` prefix is already declared in the gen-owl output, so no new prefix
handling is required.

---

## Gap 5 — `description:` emitted as `skos:definition` instead of `rdfs:comment`; `comments:` as `skos:note` instead of `skos:scopeNote`

### Description

This is a vocabulary difference rather than a missing emission, but it causes
a round-trip mismatch when comparing gen-owl output to an upstream OWL file
that uses the SKOS/RDFS conventions common in OWL ontologies:

| Schema field  | gen-owl emits       | Upstream convention      |
|---------------|---------------------|--------------------------|
| `description:` | `skos:definition`  | `rdfs:comment`           |
| `comments:`   | `skos:note`         | `skos:scopeNote`         |
| element name  | `rdfs:label`        | `skos:prefLabel`         |

Both `skos:definition` and `rdfs:comment` are valid places for a natural-language
description, but tools and SPARQL queries targeting `rdfs:comment` will miss
the content.

### Minimal reproducer

```yaml
classes:
  Foo:
    description: A foo thing.
    comments:
      - Commonly used in bar contexts.
```

gen-owl output:
```turtle
test:Foo skos:definition "A foo thing." ;
         skos:note "Commonly used in bar contexts." .
```

Expected (to match `rdfs:comment`/`skos:scopeNote` convention):
```turtle
test:Foo rdfs:comment "A foo thing." ;
         skos:scopeNote "Commonly used in bar contexts." .
```

### Suggested fix

Add generator options to `OwlSchemaGenerator` to control annotation property
selection per field:
- `--description-slot {skos:definition|rdfs:comment}` (default: `skos:definition`)
- `--comments-slot {skos:note|skos:scopeNote}` (default: `skos:note`)
- `--name-slot {rdfs:label|skos:prefLabel}` (default: `rdfs:label`)

---

## Gap 6 — `rdfs:isDefinedBy` not emitted

### Description

The upstream gist ontology annotates every entity with `rdfs:isDefinedBy`
pointing to the versioned ontology IRI
(`https://w3id.org/semanticarts/ontology/gistCore14.1.0`). This is a standard
practice in OWL ontologies that enables tools and reasoners to trace each term
to its defining module.

The LinkML metamodel has no direct equivalent, and `gen-owl` never emits
`rdfs:isDefinedBy`. The gistl schema's `id:` and `source_file:` metadata
carry analogous information but are not propagated to individual entities in the
OWL output.

The upstream gist 14.1.0 ontology has 216 `rdfs:isDefinedBy` triples (one per
named class or property). The gen-owl output has 0.

### Minimal reproducer

```yaml
id: https://example.org/test
name: test
prefixes:
  linkml: https://w3id.org/linkml/
  test: https://example.org/test/
default_prefix: test
imports:
  - linkml:types

classes:
  Foo:
    description: A foo thing.
```

Expected:
```turtle
test:Foo rdfs:isDefinedBy <https://example.org/test> .
```

Actual: no `rdfs:isDefinedBy` triple emitted.

### Suggested fix

In `owlgen.py`, after emitting each `owl:Class` / `owl:ObjectProperty` /
`owl:DatatypeProperty`, emit:
```turtle
<entity_uri> rdfs:isDefinedBy <schema_id> .
```
where `<schema_id>` is the schema's `id:` field. This provides round-trip
fidelity with ontologies that annotate every term with its defining module.

---

## Gap 7 — `exact_mappings:` emitted as `skos:exactMatch` instead of `owl:equivalentClass`

### Description

LinkML `exact_mappings:` on a class is semantically equivalent to
`owl:equivalentClass` when the mapped URI is a named class in another
ontology. `gen-owl` emits `skos:exactMatch` instead, which is a SKOS
concept-matching predicate rather than an OWL class-level axiom.

The difference matters for OWL reasoners: `skos:exactMatch` is not processed
by DL reasoners, while `owl:equivalentClass` enables entailments (e.g.
inheriting the superclasses of the equivalent class).

### Minimal reproducer

```yaml
classes:
  Duration:
    exact_mappings:
      - schema:Duration
```

gen-owl output:
```turtle
test:Duration skos:exactMatch schema:Duration .
```

Expected (for OWL round-trip fidelity):
```turtle
test:Duration owl:equivalentClass schema:Duration .
```

### Suggested fix

In `owlgen.py`, when the `exact_mappings` target resolves to a named URI
(not a blank node / OWL expression), emit `owl:equivalentClass` rather than
`skos:exactMatch`. For slot-level `exact_mappings`, emit
`owl:equivalentProperty`.

---

## Gap 8 — `any_of:` with class ranges does not produce `owl:ObjectProperty`

**Status: ✅ Resolved via `implements:` workaround.** The underlying gen-owl
behaviour is still as described below, but [scripts/gen_linkml.py](scripts/gen_linkml.py)
now emits an explicit `implements: [owl:ObjectProperty | owl:DatatypeProperty |
owl:AnnotationProperty]` on every slot. `gen-owl`'s `slot_owl_type()` honours
`implements` and bypasses range-based inference, so all 66 object properties,
50 datatype properties and 4 annotation properties round-trip to the correct
OWL property type. An upstream fix is still desirable so that schemas relying
only on `any_of:` work without the explicit `implements:` annotation.

### Description

`gen-owl` classifies a slot as `owl:ObjectProperty` or `owl:DatatypeProperty`
based exclusively on the slot's top-level `range:` value. When `range:` is
absent but `any_of:` contains class ranges, `gen-owl` still emits
`owl:DatatypeProperty`.

This affects all slots that model polymorphic object references — where a
property can point to multiple alternative classes and no single top-level
`range:` is declared. The gist ontology contains 45 `owl:ObjectProperty`
declarations without a strict `rdfs:range` (only soft `gist:rangeIncludes`
hints or no range at all). Without the workaround, all 45 are emitted as
`owl:DatatypeProperty` by `gen-owl` even when the schema has `any_of:` with
class options.

### Minimal reproducer

```yaml
slots:
  is_member_of:
    multivalued: true
    any_of:
      - range: Organization   # both are classes
      - range: Collection
```

gen-owl output (without workaround):
```turtle
test:is_member_of a owl:DatatypeProperty .
```

Expected:
```turtle
test:is_member_of a owl:ObjectProperty .
```

### Workaround (currently applied)

Add `implements: [owl:ObjectProperty]` to the slot. `slot_owl_type()` in
`owlgen.py` honours `implements` first and emits the correct property type.

```yaml
slots:
  is_member_of:
    implements:
      - owl:ObjectProperty
    multivalued: true
    any_of:
      - range: Organization
      - range: Collection
```

### Suggested upstream fix

In `owlgen.py`, when computing DP vs OP, also inspect `slot.any_of` for
`range:` references. If all resolvable range references in `any_of` are
class definitions (not built-in types), classify the slot as
`owl:ObjectProperty`. This would remove the need for the explicit
`implements:` annotation.

---

## Summary table

| Gap | Schema syntax | OWL target | Status |
|-----|--------------|------------|--------|
| Disjoint classes / properties | `disjoint_with:` | `owl:disjointWith` / `owl:propertyDisjointWith` | Not emitted |
| Deprecated elements | `deprecated: 'true'` | `owl:deprecated true` | Not emitted |
| Functional property | *(no metamodel slot)* | `owl:FunctionalProperty` | No syntax available (semantically captured as `maximum_cardinality: 1`) |
| Inverse-functional property | *(no metamodel slot)* | `owl:InverseFunctionalProperty` | No syntax available |
| Examples | `examples:` | `skos:example` | Not emitted |
| Description vocabulary | `description:` | `rdfs:comment` | Uses `skos:definition` instead |
| Comments vocabulary | `comments:` | `skos:scopeNote` | Uses `skos:note` instead |
| Defining module | *(no metamodel slot)* | `rdfs:isDefinedBy` | Not emitted |
| Exact mappings vocabulary | `exact_mappings:` | `owl:equivalentClass` | Uses `skos:exactMatch` instead |
| `any_of:` class ranges ignored for OP/DP | `any_of: [{range: MyClass}]` | `owl:ObjectProperty` | ✅ Resolved via `implements: [owl:ObjectProperty]` workaround |
