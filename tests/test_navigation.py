import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.config import PAGES, ROOT

def test_pages_exist():
    for path, _ in PAGES:
        assert (ROOT / path).exists(), path
