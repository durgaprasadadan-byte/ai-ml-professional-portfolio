import streamlit as st
from utils.config import ROOT
from utils.helpers import finish_page, setup_page

setup_page("Learning & Research")
st.title("Learning and Research")
st.write("Presentations, academic projects, learning notes, architecture walkthroughs, and tutorials. "
         "Drop `.md` files into `projects/<name>/` and PDFs into `assets/`; they appear below.")
md = sorted(ROOT.glob("projects/**/*.md")); pdfs = sorted(ROOT.glob("assets/**/*.pdf"))
tab1, tab2 = st.tabs(["Markdown notes", "PDF documents"])
with tab1:
    for f in md:
        with st.expander(str(f.relative_to(ROOT))): st.markdown(f.read_text(encoding="utf-8"))
    if not md: st.caption("No notes yet.")
with tab2:
    for f in pdfs:
        st.download_button(f.name, f.read_bytes(), file_name=f.name, key=str(f))
    if not pdfs: st.caption("No PDFs yet.")
finish_page()
