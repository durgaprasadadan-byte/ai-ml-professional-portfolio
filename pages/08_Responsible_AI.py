import streamlit as st
from utils.helpers import finish_page, setup_page, stage_list

setup_page("Responsible AI")
st.title("Responsible AI and Governance")
st.info("Academic and research analysis. Not professional implementation experience.", icon="🎓")
stage_list([(t, "[Edit with your academic notes.]") for t in [
 "Responsible AI", "AI fairness", "Bias assessment", "Explainability", "Transparency", "Accountability",
 "AI governance", "Risk assessment", "Human oversight", "Harm pathways"]])
st.header("Case study: Google Shopping ranking and advertising system")
st.write("Governance decisions in ranking and advertising systems can affect:")
for s in ["**Organizational trust**: users and advertisers rely on transparent, fair ranking.",
          "**Regulatory scrutiny**: self-preferencing and transparency concerns attract oversight.",
          "**Operational costs**: audits, remediation, and compliance programs.",
          "**Model accountability**: clear ownership, documentation, and review of ranking decisions."]:
    st.markdown(f"- {s}")
st.caption("Add specific facts and citations from your coursework before publishing.")
finish_page()
