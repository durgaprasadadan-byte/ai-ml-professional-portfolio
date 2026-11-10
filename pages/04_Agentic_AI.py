import streamlit as st
from components.architecture_viewer import mermaid, render_architecture
from utils.data_loader import load
from utils.helpers import conceptual_notice, finish_page, setup_page, stage_list

setup_page("Agentic AI")
st.title("Agentic AI")
conceptual_notice()
stage_list([(t, d) for t, d in [
 ("Agent architecture", "Reasoning loop, tools, memory, and guardrails."),
 ("Agent orchestration", "Graph-based control flow with LangGraph."),
 ("Multi-agent workflows", "Specialist agents coordinated by a supervisor."),
 ("Tool calling", "Model selects tools and supplies structured arguments."),
 ("Function calling", "Typed function schemas validated before execution."),
 ("Memory management", "Short-term state and long-term stored context."),
 ("Planning and execution", "Decompose tasks, execute steps, re-plan on failure."),
 ("Human-in-the-loop", "Approval gates for sensitive actions."),
 ("MCP integration", "Expose tools and data through Model Context Protocol servers."),
 ("API integration", "FastAPI services as tool backends."),
 ("Error handling", "Retries, timeouts, step limits, graceful fallbacks."),
 ("Evaluation and observability", "Trace runs and score task success.")]])
st.write("References: LangGraph · LangChain · Amazon Bedrock · MCP · FastAPI · Python · Docker")
render_architecture("Agentic", load("architectures")["Agentic AI architecture"])
st.subheader("Example use cases")
mermaid("flowchart LR\nR[Request]-->P[Plan]-->T[Call tools]-->C{Sensitive?}\nC-- yes -->H[Human approval]-->A[Act]\nC-- no -->A-->S[Summarize]", 300)
st.subheader("Future learning areas")
st.caption("Learning goals only. No implementation experience is implied.")
st.write("AutoGen · CrewAI · other agent frameworks")
finish_page()
