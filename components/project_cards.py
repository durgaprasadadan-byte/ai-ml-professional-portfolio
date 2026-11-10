"""Project cards and the 20-section case study template."""
import streamlit as st

from utils.config import PLACEHOLDER
from utils.helpers import badges

CASE_SECTIONS = [
    ("Project overview", "overview"), ("Business problem", "business_problem"), ("Objectives", "objectives"),
    ("Proposed solution", "solution"), ("Project type and implementation status", None),
    ("Technical architecture", "architecture"), ("Technology stack", None), ("Data sources", "data_sources"),
    ("Implementation methodology", "methodology"), ("Model or system development", "development"),
    ("API and application integration", "integration"), ("Testing and validation", "testing"),
    ("Performance evaluation", "evaluation"), ("Results and outcomes", "results"),
    ("Technical challenges", "challenges"), ("Lessons learned", "lessons"),
    ("Future improvements", "future"), ("GitHub repository link", "github"),
    ("Technical documentation", "docs"), ("Demonstration link", "demo"),
]


def project_card(p: dict) -> None:
    st.markdown(
        f'<div class="card"><h4>{p["name"]}</h4>'
        f'{badges([p["category"]])}{badges([p["type"]], "type")}{badges([p["status"]], "status")}'
        f'<p>{p.get("short_description", PLACEHOLDER)}</p>'
        f'<div>{badges(p.get("stack", []))}</div></div>', unsafe_allow_html=True)
    if st.button("View Details", key=f"view_{p['id']}"):
        st.query_params["project"] = p["id"]
        st.rerun()


def case_study(p: dict) -> None:
    """Render the standard 20-section case study."""
    st.header(p["name"])
    cs = p.get("case_study", {})
    for i, (title, key) in enumerate(CASE_SECTIONS, 1):
        st.subheader(f"{i}. {title}")
        if title.startswith("Project type"):
            st.markdown(badges([p["type"]], "type") + badges([p["status"]], "status"), unsafe_allow_html=True)
        elif title == "Technology stack":
            st.markdown(badges(p.get("stack", [])), unsafe_allow_html=True)
        else:
            val = cs.get(key) or ""
            if val.startswith("http"):
                st.markdown(f"[{val}]({val})")
            else:
                st.write(val or PLACEHOLDER)
