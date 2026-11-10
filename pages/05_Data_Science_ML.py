import pandas as pd
import plotly.express as px
import streamlit as st
from components.metrics import metric_row
from utils.helpers import finish_page, setup_page

setup_page("Data Science & ML")
st.title("Data Science and Machine Learning")
SECTIONS = ["Problem definition", "Dataset overview", "Data preprocessing", "Feature engineering", "Model selection",
            "Training", "Validation", "Evaluation", "Results", "Limitations"]
tabs = st.tabs(["Fraud detection", "Customer segmentation", "E-commerce analytics", "Churn prediction", "Predictive modeling"])
with tabs[0]:
    st.caption("Academic project. Documented results only.")
    metric_row([("Transactions", "10,000"), ("Features", "20"), ("Legitimate", "8,749"), ("Fraudulent", "1,251 (12.5%)")])
    df = pd.DataFrame([
        ("Random Forest - Raw", 94.68, 0.9738, 0.8360),
        ("Random Forest - Engineered", 94.64, 0.9766, 0.8508),
        ("Gradient Boosting - Raw", 94.88, 0.9778, 0.8624)],
        columns=["Model", "Accuracy (%)", "ROC-AUC", "Average Precision"])
    st.dataframe(df, hide_index=True, use_container_width=True)
    m = st.radio("Metric", ["ROC-AUC", "Average Precision", "Accuracy (%)"], horizontal=True)
    fig = px.bar(df, x="Model", y=m, text=m, color="Model")
    fig.update_layout(showlegend=False)
    if m != "Accuracy (%)": fig.update_yaxes(range=[0.8 if m == "Average Precision" else 0.95, 1])
    else: fig.update_yaxes(range=[90, 100])
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Truncated y-axis for readability. Precision, recall, F1 and confusion-matrix values are not reported here because they were not provided.")
    with st.expander("Case-study sections"):
        for s in SECTIONS: st.markdown(f"- **{s}**: [edit with documented details]")
for t, name in zip(tabs[1:], ["Customer segmentation", "E-commerce analytics", "Customer churn prediction", "Predictive modeling"]):
    with t:
        st.info(f"{name}: placeholder. Add documented details and label the project type. Use synthetic data for public demos.")
        for s in SECTIONS: st.markdown(f"- **{s}**: [to be documented]")
finish_page()
