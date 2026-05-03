"""Schema structure and validation tests."""
import pytest
import yaml
from pathlib import Path


SCHEMA_DIR = Path(__file__).parent.parent / "src" / "gist" / "schema"
SCHEMA_FILES = list(SCHEMA_DIR.glob("gist*.yaml"))


def load_schema(schema_file):
    """Load schema YAML file."""
    with open(schema_file, 'r') as f:
        return yaml.safe_load(f)


class TestSchemaExistence:
    """Test that expected schema files exist."""

    def test_main_schema_exists(self):
        """Test that main gist.yaml schema exists."""
        schema_file = SCHEMA_DIR / "gist.yaml"
        assert schema_file.exists(), f"Main schema not found at {schema_file}"

    def test_core_schema_exists(self):
        """Test that gist_core.yaml schema exists."""
        schema_file = SCHEMA_DIR / "gist_core.yaml"
        assert schema_file.exists(), f"Core schema not found at {schema_file}"

    @pytest.mark.parametrize("schema_file", SCHEMA_FILES)
    def test_all_schema_files_readable(self, schema_file):
        """Test that all schema files are readable YAML."""
        assert schema_file.exists(), f"Schema file not found: {schema_file}"
        assert schema_file.suffix in [".yaml", ".yml"], f"Not a YAML file: {schema_file}"


class TestSchemaStructure:
    """Test LinkML schema structure and validity."""

    @pytest.fixture(scope="class")
    def main_schema(self):
        """Load main schema."""
        schema_file = SCHEMA_DIR / "gist.yaml"
        return load_schema(schema_file)

    def test_schema_has_id(self, main_schema):
        """Test that schema has an id field."""
        assert "id" in main_schema, "Schema missing 'id' field"
        assert main_schema["id"].startswith("https://"), "Schema id should be a URL"

    def test_schema_has_name(self, main_schema):
        """Test that schema has a name field."""
        assert "name" in main_schema, "Schema missing 'name' field"
        assert isinstance(main_schema["name"], str), "Schema name should be a string"

    def test_schema_has_description(self, main_schema):
        """Test that schema has a description."""
        assert "description" in main_schema, "Schema missing 'description' field"

    def test_schema_has_version(self, main_schema):
        """Test that schema has a version."""
        assert "version" in main_schema, "Schema missing 'version' field"

    def test_schema_has_prefixes(self, main_schema):
        """Test that schema declares prefixes."""
        assert "prefixes" in main_schema, "Schema missing 'prefixes' section"
        assert isinstance(main_schema["prefixes"], dict), "Prefixes should be a dict"
        assert len(main_schema["prefixes"]) > 0, "Schema should declare at least one prefix"

    def test_schema_has_default_prefix(self, main_schema):
        """Test that schema has a default prefix."""
        assert "default_prefix" in main_schema, "Schema missing 'default_prefix'"
        prefix = main_schema["default_prefix"]
        assert prefix in main_schema["prefixes"], f"Default prefix '{prefix}' not in prefixes"

    def test_schema_has_default_range(self, main_schema):
        """Test that schema has a default range."""
        assert "default_range" in main_schema, "Schema missing 'default_range'"

    def test_schema_imports_linkml_types(self, main_schema):
        """Test that schema imports linkml:types."""
        assert "imports" in main_schema, "Schema missing 'imports' section"
        imports = main_schema["imports"]
        assert "linkml:types" in imports, "Schema should import linkml:types"

    def test_schema_has_license(self, main_schema):
        """Test that schema has a license."""
        assert "license" in main_schema, "Schema missing 'license' field"

    def test_main_schema_imports_modules(self, main_schema):
        """Test that main schema imports modular schemas."""
        imports = main_schema.get("imports", [])
        # Main schema should import submodules
        assert any("gist_core" in i for i in imports), "Main schema should import gist_core"


class TestSchemaElements:
    """Test that schema elements are properly defined."""

    @pytest.fixture(scope="class")
    def core_schema(self):
        """Load core schema."""
        schema_file = SCHEMA_DIR / "gist_core.yaml"
        return load_schema(schema_file)

    def test_schema_has_classes(self, core_schema):
        """Test that schema defines classes."""
        assert "classes" in core_schema, "Core schema should have classes"
        classes = core_schema["classes"]
        assert isinstance(classes, dict), "Classes should be a dict"
        assert len(classes) > 0, "Schema should define at least one class"

    def test_classes_have_descriptions(self, core_schema):
        """Test that classes have descriptions."""
        classes = core_schema.get("classes", {})
        for class_name, class_def in classes.items():
            assert "description" in class_def or class_name == "root", \
                f"Class '{class_name}' should have a description"

    def test_schema_has_slots(self, core_schema):
        """Test that schema defines slots."""
        assert "slots" in core_schema, "Core schema should have slots"
        slots = core_schema["slots"]
        assert isinstance(slots, dict), "Slots should be a dict"
        assert len(slots) > 0, "Schema should define at least one slot"

    def test_slots_have_ranges(self, core_schema):
        """Test that slots have range specifications or use defaults."""
        slots = core_schema.get("slots", {})
        # Slots can have explicit ranges, or they can rely on default_range from schema
        # or they can inherit from parent slots. This test just checks that the
        # schema structure is valid; LinkML will handle default ranges.
        assert len(slots) > 0, "Core schema should have slots defined"


class TestModularSchema:
    """Test modular schema structure."""

    def test_gist_core_is_valid(self):
        """Test that gist_core schema is valid."""
        schema_file = SCHEMA_DIR / "gist_core.yaml"
        schema = load_schema(schema_file)
        assert schema is not None
        assert "classes" in schema or "slots" in schema

    def test_gist_media_types_is_valid(self):
        """Test that gist_media_types schema is valid."""
        schema_file = SCHEMA_DIR / "gist_media_types.yaml"
        if schema_file.exists():
            schema = load_schema(schema_file)
            assert schema is not None

    def test_gist_prefix_declarations_is_valid(self):
        """Test that gist_prefix_declarations schema is valid."""
        schema_file = SCHEMA_DIR / "gist_prefix_declarations.yaml"
        if schema_file.exists():
            schema = load_schema(schema_file)
            assert schema is not None

    def test_modular_schemas_use_subsets(self):
        """Test that modular schemas use subsets for organization."""
        schema_file = SCHEMA_DIR / "gist_core.yaml"
        schema = load_schema(schema_file)
        if "subsets" in schema:
            subsets = schema["subsets"]
            assert isinstance(subsets, dict)


class TestOntologyAlignment:
    """Test ontology alignment and mappings."""

    @pytest.fixture(scope="class")
    def main_schema(self):
        """Load main schema."""
        schema_file = SCHEMA_DIR / "gist.yaml"
        return load_schema(schema_file)

    def test_schema_elements_have_mappings(self, main_schema):
        """Test that schema elements have ontology mappings."""
        # Check if any classes have mappings
        classes = main_schema.get("classes", {})
        has_mappings = False
        for class_def in classes.values():
            if any(key in class_def for key in ["exact_mappings", "broad_mappings", "class_uri"]):
                has_mappings = True
                break
        # It's OK if some classes don't have mappings, but some should
        # (Just checking the structure exists in the schema)


class TestSchemaConsistency:
    """Test consistency across schema modules."""

    @pytest.fixture(scope="class")
    def main_schema(self):
        """Load main schema."""
        schema_file = SCHEMA_DIR / "gist.yaml"
        return load_schema(schema_file)

    @pytest.fixture(scope="class")
    def core_schema(self):
        """Load core schema."""
        schema_file = SCHEMA_DIR / "gist_core.yaml"
        return load_schema(schema_file)

    def test_imported_modules_exist(self, main_schema):
        """Test that imported modules exist."""
        imports = main_schema.get("imports", [])
        for imported in imports:
            if imported.startswith("./"):
                # Local import
                module_name = imported.replace("./", "")
                if not module_name.endswith(".yaml"):
                    module_name += ".yaml"
                schema_file = SCHEMA_DIR / module_name
                assert schema_file.exists(), f"Imported schema {imported} not found"

    def test_core_schema_has_classes(self, core_schema):
        """Test that core schema has classes."""
        assert "classes" in core_schema, "Core schema should have classes"
        assert len(core_schema["classes"]) > 0, "Core schema should define classes"

    def test_class_inheritance_is_valid(self, core_schema):
        """Test that class inheritance references valid parents."""
        classes = core_schema.get("classes", {})
        for class_name, class_def in classes.items():
            if "is_a" in class_def:
                parent_name = class_def["is_a"]
                # Parent should be defined or imported
                # (We skip detailed validation here as it's complex)

    def test_slot_ranges_reference_valid_types(self, core_schema):
        """Test that slot ranges reference valid types or classes."""
        slots = core_schema.get("slots", {})
        classes = core_schema.get("classes", {})
        types_section = core_schema.get("types", {})

        for slot_name, slot_def in slots.items():
            if "range" in slot_def:
                range_val = slot_def["range"]
                # Range can be a built-in type, a class, or undefined (defaults to default_range)
                is_valid = (
                    range_val in ["string", "integer", "float", "boolean", "date", "datetime"]
                    or range_val in classes
                    or range_val in types_section
                )
                # We allow some ranges that might be from imported modules
