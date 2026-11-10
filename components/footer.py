"""Consistent footer."""
import streamlit as st


def render_footer() -> None:
    st.markdown('<div class="footer">Built with Streamlit · Content is configurable via <code>data/*.json</code> · '
                'Synthetic data only in public demos</div>', unsafe_allow_html=True)
