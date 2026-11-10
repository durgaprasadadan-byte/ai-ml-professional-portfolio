"""Portfolio home page (Streamlit entry point)."""
import streamlit as st

from components.metrics import metric_row
from components.project_cards import project_card
from utils.config import HEADLINE
from utils.data_loader import load
from utils.helpers import badges, finish_page, setup_page

setup_page("Home")
profile, projects, skills = load("profile"), load("projects"), load("skills")

st.markdown(f'<div class="hero"><h1>{profile["name"]}</h1><div class="tag">{HEADLINE}</div></div>', unsafe_allow_html=True)
st.write(profile["summary"])
c = st.columns(3)
if profile.get("github"): c[0].link_button("GitHub", profile["github"])
if profile.get("linkedin"): c[1].link_button("LinkedIn", profile["linkedin"])
c[2].page_link("pages/10_Resume.py", label="Resume & download")

st.subheader("Specialization")
metric_row([("Focus", "GenAI & RAG"), ("Systems", "Agentic AI"), ("Foundations", "ML / DL / NLP"), ("Platform", "Cloud AI")])
st.subheader("Featured projects")
for p in projects[:3]:
    project_card(p)
if st.query_params.get("project"):
    st.switch_page("pages/02_AI_ML_Projects.py")
st.subheader("Core technologies")
st.markdown(badges([s for cat in ("Generative AI", "Cloud", "Backend") for s in skills[cat]]), unsafe_allow_html=True)
st.subheader("Experience highlights")
st.caption("Employer details are configurable in data/experience.json.")
st.page_link("pages/01_Professional_Experience.py", label="View career timeline →")
finish_page()
