import streamlit as st
from components.architecture_viewer import render_architecture
from utils.data_loader import load
from utils.helpers import conceptual_notice, finish_page, setup_page, stage_list

setup_page("Generative AI")
st.title("Generative AI Projects")
st.header("Enterprise GenAI Application for Customer and Account Intelligence")
conceptual_notice("The pipeline below is a conceptual reference. Mark components as implemented/tested in data/projects.json only when verified.")
stage_list([
 ("Business requirements", "Define users, questions to answer, accuracy needs, and compliance constraints."),
 ("Data ingestion", "Connect approved sources and track provenance."),
 ("Document processing", "Parse and clean documents; handle tables and metadata."),
 ("Text chunking", "Split text into overlapping, semantically coherent chunks."),
 ("Embedding generation", "Convert chunks to vectors with an embedding model."),
 ("Vector database", "Index vectors with metadata for filtered similarity search."),
 ("Retrieval-Augmented Generation", "Retrieve relevant chunks and supply them as context."),
 ("LLM integration", "Call the model (e.g. via Amazon Bedrock) behind a FastAPI service."),
 ("Prompt engineering", "Design system prompts, grounding rules, and output formats."),
 ("Response generation", "Generate answers with citations to source chunks."),
 ("Evaluation", "Measure retrieval quality, groundedness, and answer quality; track in MLflow."),
 ("Monitoring", "Track latency, cost, errors, and feedback signals."),
])
st.subheader("Technology references")
st.write("Python · Amazon Bedrock · LangChain · LangGraph · Vector databases · FastAPI · Docker · AWS · MLflow")
st.subheader("Architecture")
render_architecture("RAG", load("architectures")["RAG architecture"])
st.page_link("pages/02_AI_ML_Projects.py", label="Open the project case study →")
finish_page()
