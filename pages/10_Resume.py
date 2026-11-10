import streamlit as st
from utils.config import PLACEHOLDER, RESUME_PDF
from utils.data_loader import load
from utils.helpers import badges, finish_page, setup_page

setup_page("Resume")
st.title("Resume")
p, skills, exp = load("profile"), load("skills"), load("experience")
if RESUME_PDF.exists():
    st.download_button("Download PDF resume", RESUME_PDF.read_bytes(), "resume.pdf", "application/pdf")
else:
    st.warning("Resume not available. Add your PDF at assets/resume/resume.pdf.", icon="📄")
st.subheader("Professional summary"); st.write(p["summary"])
st.subheader("Technical skills")
for k, v in skills.items(): st.markdown(f"**{k}** " + badges(v), unsafe_allow_html=True)
st.subheader("Work experience")
for e in exp: st.markdown(f"- **{e['organization']}**: {e.get('title') or PLACEHOLDER} ({e.get('period') or PLACEHOLDER})")
st.subheader("Education")
for ed in p.get("education", []): st.markdown(f"- {ed['degree']}, {ed['institution']} ({ed['year']})")
st.subheader("Certifications")
for c in p.get("certifications") or []: st.markdown(f"- {c}")
if not p.get("certifications"): st.caption(PLACEHOLDER)
finish_page()
