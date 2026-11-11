import streamlit as st
from components.experience_timeline import render_timeline
from utils.data_loader import load
from utils.helpers import finish_page, setup_page

setup_page("Experience")
st.title("Professional Experience")
st.warning("Add only verified, non-confidential details in data/experience.json.", icon="⚠️")
render_timeline(load("experience"))
finish_page()
