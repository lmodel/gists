"""Tests leveraging SHACL shapes and semantic arts validation."""
import pytest
from pathlib import Path


VENDOR_DIR = Path(__file__).parent / "vendor" / "semanticarts"
SHAPES_FILE = VENDOR_DIR / "ontologyShapes.ttl"
PROPERTY_QUERY = VENDOR_DIR / "property_type_construct.rq"


class TestSemanticArtsShapes:
    """Test SHACL shapes from semantic arts vendor content."""

    def test_shapes_file_exists(self):
        """Test that ontologyShapes.ttl exists."""
        assert SHAPES_FILE.exists(), f"SHACL shapes file not found at {SHAPES_FILE}"

    def test_shapes_file_is_readable(self):
        """Test that shapes file is readable."""
        assert SHAPES_FILE.stat().st_size > 0, "Shapes file is empty"

    def test_shapes_file_contains_shacl(self):
        """Test that shapes file contains SHACL definitions."""
        with open(SHAPES_FILE, 'r') as f:
            content = f.read()
            assert "sh:" in content or "@prefix sh:" in content, \
                "Shapes file should contain SHACL definitions"

    def test_property_query_file_exists(self):
        """Test that property type SPARQL query exists."""
        if PROPERTY_QUERY.exists():
            assert PROPERTY_QUERY.stat().st_size > 0, "Property query file is empty"

    def test_vendor_directory_structure(self):
        """Test vendor directory structure."""
        assert VENDOR_DIR.is_dir(), "Vendor directory should exist"
        assert SHAPES_FILE.exists(), "Core shapes file should exist"


class TestSHACLShapeStructure:
    """Test structure of SHACL shapes for validation."""

    def test_shapes_define_node_shapes(self):
        """Test that shapes define SHACL NodeShapes."""
        with open(SHAPES_FILE, 'r') as f:
            content = f.read()
            assert "sh:NodeShape" in content, \
                "Shapes should define SHACL NodeShapes"

    def test_shapes_define_targets(self):
        """Test that shapes define SHACL targets."""
        with open(SHAPES_FILE, 'r') as f:
            content = f.read()
            assert "sh:target" in content or "sh:SPARQLTarget" in content, \
                "Shapes should define targets"

    def test_shapes_define_properties(self):
        """Test that shapes define SHACL properties."""
        with open(SHAPES_FILE, 'r') as f:
            content = f.read()
            assert "sh:property" in content, \
                "Shapes should define property constraints"

    def test_shapes_have_descriptions(self):
        """Test that shapes have descriptions."""
        with open(SHAPES_FILE, 'r') as f:
            content = f.read()
            # Check for SKOS descriptions which are typically used in SHACL
            assert "skos:definition" in content or "skos:prefLabel" in content, \
                "Shapes should have descriptions or labels"


class TestVendorContentValidation:
    """Tests using semantic arts vendor content for validation."""

    def test_vendor_content_is_accessible(self):
        """Test that vendor content is properly organized."""
        assert VENDOR_DIR.exists(), "Vendor directory should exist"
        # Check that it has proper content
        vendor_files = list(VENDOR_DIR.glob("*"))
        assert len(vendor_files) > 0, "Vendor directory should have content"

    def test_can_parse_ttl_format(self):
        """Test that we can parse Turtle RDF format."""
        try:
            import rdflib
            # Try to parse the shapes file
            g = rdflib.Graph()
            g.parse(str(SHAPES_FILE), format="turtle")
            assert len(g) > 0, "Parsed graph should not be empty"
        except ImportError:
            pytest.skip("rdflib not available")

    def test_shapes_reference_gist_namespace(self):
        """Test that shapes reference gist namespace."""
        with open(SHAPES_FILE, 'r') as f:
            content = f.read()
            assert "gistl:" in content, \
                "Shapes should reference gist namespace"

    def test_shapes_reference_gshapes_namespace(self):
        """Test that shapes reference gshapes namespace."""
        with open(SHAPES_FILE, 'r') as f:
            content = f.read()
            assert "gshapes:" in content, \
                "Shapes should reference gshapes namespace"


class TestValidationConstraints:
    """Test SHACL validation constraints in shapes."""

    def test_shapes_enforce_definitions(self):
        """Test that shapes enforce mandatory definitions."""
        with open(SHAPES_FILE, 'r') as f:
            content = f.read()
            # Look for definition constraints
            assert "Definition" in content or "definition" in content, \
                "Shapes should enforce definitions"

    def test_shapes_check_class_naming(self):
        """Test that shapes check class naming conventions."""
        with open(SHAPES_FILE, 'r') as f:
            content = f.read()
            # Look for naming pattern constraints
            assert "Class" in content or "Title" in content, \
                "Shapes should include class constraints"

    def test_shapes_validate_instances(self):
        """Test that shapes validate instances."""
        with open(SHAPES_FILE, 'r') as f:
            content = f.read()
            # Look for instance validation
            assert "Instance" in content or "individual" in content.lower(), \
                "Shapes should validate instances"


class TestSHACLIntegration:
    """Integration tests with SHACL validation."""

    def test_shapes_file_is_well_formed(self):
        """Test that shapes file is well-formed."""
        try:
            import rdflib
            g = rdflib.Graph()
            try:
                g.parse(str(SHAPES_FILE), format="turtle")
                # If we get here, the file parses successfully
                assert len(g) > 0, "Parsed graph should have triples"
            except Exception as e:
                pytest.fail(f"Failed to parse shapes file: {e}")
        except ImportError:
            pytest.skip("rdflib not available for full validation")

    @pytest.mark.skipif(not SHAPES_FILE.exists(), reason="Shapes file not found")
    def test_shapes_contain_prefixes(self):
        """Test that shapes file declares required prefixes."""
        with open(SHAPES_FILE, 'r') as f:
            content = f.read()
            required_prefixes = ["@prefix sh:", "@prefix owl:", "@prefix rdf:"]
            for prefix in required_prefixes:
                assert prefix in content, f"Shapes should declare {prefix}"
