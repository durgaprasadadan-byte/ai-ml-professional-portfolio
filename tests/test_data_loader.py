import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import pytest
from utils.config import DATA_DIR, PAGES, ROOT
from utils.data_loader import REQUIRED, load_json_file

@pytest.mark.parametrize("name,typ", REQUIRED.items())
def test_json_valid(name, typ):
    assert isinstance(load_json_file(DATA_DIR / f"{name}.json", typ), typ)

def test_project_fields():
    for p in load_json_file(DATA_DIR / "projects.json", list):
        for k in ("id", "name", "category", "type", "status", "stack"):
            assert k in p

def test_bad_json(tmp_path):
    f = tmp_path / "x.json"; f.write_text("{bad")
    with pytest.raises(ValueError): load_json_file(f, dict)
