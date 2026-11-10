import streamlit as st
from utils.data_loader import load
from utils.helpers import finish_page, setup_page

setup_page("Contact")
st.title("Contact")
st.write("Open to collaboration on AI/ML engineering, GenAI, and agentic AI work. Reach out via the channels below.")
p = load("profile")
shown = False
if p.get("email"): st.markdown(f"**Email:** {p['email']}"); shown = True
if p.get("linkedin"): st.link_button("LinkedIn", p["linkedin"]); shown = True
if p.get("github"): st.link_button("GitHub", p["github"]); shown = True
if not shown: st.info("Contact details are not configured. Add email, linkedin, and github in data/profile.json.")
finish_page()
