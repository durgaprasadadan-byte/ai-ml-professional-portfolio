"""Central paths and constants."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
STYLES = ROOT / "styles" / "custom.css"
RESUME_PDF = ROOT / "assets" / "resume" / "resume.pdf"
PLACEHOLDER = "[Not provided - edit data/*.json]"

PAGES = [
    ("Home.py", "Home"),
    ("pages/01_Professional_Experience.py", "Experience"),
    ("pages/02_AI_ML_Projects.py", "Projects"),
    ("pages/03_Generative_AI.py", "Generative AI"),
    ("pages/04_Agentic_AI.py", "Agentic AI"),
    ("pages/05_Data_Science_ML.py", "Data Science & ML"),
    ("pages/06_System_Architecture.py", "Architecture"),
    ("pages/07_Technical_Skills.py", "Skills"),
    ("pages/08_Responsible_AI.py", "Responsible AI"),
    ("pages/09_Learning_Research.py", "Learning & Research"),
    ("pages/10_Resume.py", "Resume"),
    ("pages/11_Contact.py", "Contact"),
]
HEADLINE = "AI/ML Engineer | Data Scientist | Generative AI | Agentic AI | LLM Applications | RAG"
