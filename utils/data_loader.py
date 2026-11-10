"""Validated JSON loading."""
import json
from pathlib import Path
from typing import Any

import streamlit as st

from utils.config import DATA_DIR

REQUIRED = {
    "profile": dict,
    "experience": list,
    "skills": dict,
    "projects": list,
    "architectures": dict,
}


def load_json_file(path: Path, expected: type) -> Any:
    """Load a JSON file and check its top-level type. Raises ValueError on problems."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Missing data file: {path.name}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path.name}: {exc}") from exc
    if not isinstance(data, expected):
        raise ValueError(f"{path.name} must contain a JSON {expected.__name__}")
    return data


@st.cache_data
def load(name: str) -> Any:
    """Load one of the known data files by name (e.g. 'projects')."""
    return load_json_file(DATA_DIR / f"{name}.json", REQUIRED[name])
