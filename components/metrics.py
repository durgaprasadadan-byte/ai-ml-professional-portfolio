"""Metric card row."""
import streamlit as st


def metric_row(metrics: list[tuple[str, str]]) -> None:
    for col, (label, value) in zip(st.columns(len(metrics)), metrics):
        col.metric(label, value)
