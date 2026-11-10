import streamlit as st
from components.project_cards import case_study, project_card
from utils.data_loader import load
from utils.helpers import finish_page, setup_page

setup_page("Projects")
projects = load("projects")
pid = st.query_params.get("project")
if pid:
    match = next((p for p in projects if p["id"] == pid), None)
    if st.button("← All projects"):
        st.query_params.clear(); st.rerun()
    if match: case_study(match)
    else: st.error("Project not found.")
else:
    st.title("AI/ML Projects")
    q = st.text_input("Search", placeholder="name, technology, description")
    cats = sorted({p["category"] for p in projects}); types = sorted({p["type"] for p in projects})
    c1, c2 = st.columns(2)
    sel_c = c1.multiselect("Category", cats); sel_t = c2.multiselect("Project type", types)
    def ok(p):
        hay = " ".join([p["name"], p.get("short_description", ""), *p.get("stack", [])]).lower()
        return (not q or q.lower() in hay) and (not sel_c or p["category"] in sel_c) and (not sel_t or p["type"] in sel_t)
    shown = [p for p in projects if ok(p)]
    st.caption(f"{len(shown)} project(s)")
    for p in shown: project_card(p)
finish_page()
