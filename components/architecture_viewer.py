"""Reusable architecture viewer (Mermaid via CDN, with source fallback)."""
import streamlit as st
import streamlit.components.v1 as components

FIELDS = [("System components", "components"), ("Data flow", "data_flow"), ("Component responsibilities", "responsibilities"),
          ("Technology selection", "technology"), ("Integration points", "integration"), ("Security considerations", "security"),
          ("Scalability", "scalability"), ("Failure handling", "failure"), ("Monitoring", "monitoring")]


def mermaid(code: str, height: int = 420) -> None:
    html = f"""<div class="mermaid" style="background:#fff;padding:8px;border-radius:8px">{code}</div>
    <script type="module">import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.esm.min.mjs';
    mermaid.initialize({{startOnLoad:true}});</script>"""
    components.html(html, height=height, scrolling=True)
    with st.expander("Mermaid source"):
        st.code(code, language="text")


def render_architecture(name: str, spec: dict) -> None:
    st.info(spec.get("label", "Conceptual architecture"), icon="ℹ️")
    mermaid(spec["diagram"])
    for title, key in FIELDS:
        st.markdown(f"**{title}:** {spec.get(key, '[edit data/architectures.json]')}")
