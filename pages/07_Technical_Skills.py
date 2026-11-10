import streamlit as st
from utils.data_loader import load
from utils.helpers import badges, finish_page, setup_page

setup_page("Skills")
st.title("Technical Skills")
skills = load("skills")
cols = st.columns(3)
for i, (cat, items) in enumerate(skills.items()):
    with cols[i % 3]:
        st.markdown(f'<div class="card"><h4>{cat}</h4>{badges(items)}</div>', unsafe_allow_html=True)
finish_page()
