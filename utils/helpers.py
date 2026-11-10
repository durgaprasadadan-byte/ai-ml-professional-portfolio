"""Page setup and small shared helpers."""
import streamlit as st

from components.footer import render_footer
from components.navigation import render_navigation
from utils.config import STYLES


def setup_page(title: str) -> None:
    """Configure page, inject CSS, render navigation."""
    st.set_page_config(page_title=f"{title} | AI/ML Portfolio", page_icon="🧠", layout="wide")
    try:
        st.markdown(f"<style>{STYLES.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
    except OSError:
        pass
    render_navigation()


def finish_page() -> None:
    render_footer()


def badges(items: list[str], kind: str = "") -> str:
    return "".join(f'<span class="badge {kind}">{i}</span>' for i in items)


def stage_list(stages: list[tuple[str, str]]) -> None:
    """Render numbered (title, description) stages."""
    for i, (t, d) in enumerate(stages, 1):
        with st.expander(f"{i}. {t}"):
            st.write(d)


def conceptual_notice(text: str = "Conceptual architecture / learning material. Not a claim of production deployment.") -> None:
    st.info(text, icon="ℹ️")
