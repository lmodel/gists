"""Pytest configuration: make scripts/ importable."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

# Skip test_data.py if the generated datamodel doesn't exist
datamodel_path = Path(__file__).parent.parent / "src" / "gists" / "datamodel" / "gist.py"
if not datamodel_path.exists():
    collect_ignore = ["test_data.py"]
