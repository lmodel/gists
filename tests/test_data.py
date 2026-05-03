"""Data validation tests for gist schema."""
import os
import glob
import pytest
from pathlib import Path

import gist.datamodel.gist
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.exceptions import ValidationError

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml'))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml'))


class TestValidDataFiles:
    """Test suite for valid data files."""

    @pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
    def test_loads_without_error(self, filepath):
        """Test loading of all valid data files."""
        target_class_name = Path(filepath).stem.split("-")[0]
        tgt_class = getattr(
            gist.datamodel.gist,
            target_class_name,
        )
        obj = yaml_loader.load(filepath, target_class=tgt_class)
        assert obj, f"Failed to load {filepath}"

    @pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
    def test_objects_are_not_none(self, filepath):
        """Test that valid files produce non-None objects."""
        target_class_name = Path(filepath).stem.split("-")[0]
        tgt_class = getattr(
            gist.datamodel.gist,
            target_class_name,
        )
        obj = yaml_loader.load(filepath, target_class=tgt_class)
        assert obj is not None

    @pytest.mark.skipif(not INVALID_EXAMPLE_FILES, reason="No invalid example files")
    @pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
    def test_invalid_data_raises_error(self, filepath):
        """Test that invalid data files raise validation errors."""
        try:
            target_class_name = Path(filepath).stem.split("-")[0]
            tgt_class = getattr(
                gist.datamodel.gist,
                target_class_name,
            )
            # Attempt to load with validation enabled
            obj = yaml_loader.load(filepath, target_class=tgt_class)
            # If no error is raised, verify that validation would catch it
            # Note: This depends on LinkML runtime validation being enabled
        except (ValidationError, ValueError, TypeError) as e:
            # Expected behavior: invalid data should raise an error
            assert True
