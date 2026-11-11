"""Experience timeline."""
import streamlit as st

from utils.config import PLACEHOLDER
from utils.helpers import badges


def render_timeline(entries: list[dict]) -> None:
    for e in entries:
        engagement = f"<div>{e['engagement']}</div>" if e.get("engagement") else ""
        st.markdown(
            f'<div class="card"><h4>{e.get("title") or PLACEHOLDER} · {e.get("organization", "")}</h4>'
            f'<div class="muted">{e.get("location") or PLACEHOLDER} · '
            f'{e.get("employment_type") or PLACEHOLDER} · {e.get("period") or PLACEHOLDER}</div>'
            f'{engagement}</div>',
            unsafe_allow_html=True)
        with st.expander("Details"):
            for label, key in [("Responsibilities", "responsibilities"), ("Project highlights", "highlights"),
                               ("Measurable outcomes (verified only)", "outcomes")]:
                st.markdown(f"**{label}**")
                items = e.get(key) or []
                for it in items:
                    st.markdown(f"- {it}")
                if not items:
                    st.caption(PLACEHOLDER)
            st.markdown("**Technologies**")
            st.markdown(badges(e.get("technologies") or [PLACEHOLDER]), unsafe_allow_html=True)
