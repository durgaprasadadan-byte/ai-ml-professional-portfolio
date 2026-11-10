import streamlit as st
from components.architecture_viewer import render_architecture
from utils.data_loader import load
from utils.helpers import finish_page, setup_page

setup_page("Architecture")
st.title("System Architecture")
archs = load("architectures")
choice = st.selectbox("Architecture", list(archs))
render_architecture(choice, archs[choice])
finish_page()
