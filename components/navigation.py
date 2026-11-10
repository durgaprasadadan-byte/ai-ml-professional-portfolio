"""Reusable sidebar navigation."""
import streamlit as st

from utils.config import PAGES


def render_navigation() -> None:
    with st.sidebar:
        st.markdown("### 🧠 AI/ML Portfolio")
        for path, label in PAGES:
            st.page_link(path, label=label)
