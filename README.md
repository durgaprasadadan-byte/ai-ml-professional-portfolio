# AI/ML Professional Portfolio
Streamlit portfolio. Entry point: `Home.py`.

## Run locally
```
git clone <your-repo-url> && cd ai-ml-professional-portfolio
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run Home.py
pytest
```
## Deploy (Streamlit Community Cloud)
1. Push to GitHub. 2. share.streamlit.io → New app → select repo, branch, main file `Home.py`. 3. Deploy.
Use `.streamlit/secrets.toml` (git-ignored) or the Cloud secrets UI for any future credentials.

## Customize
- Profile, links, education: `data/profile.json` (leave email/links empty to hide them)
- Experience: `data/experience.json` (verified facts only)
- Add a project: append an object to `data/projects.json` (see existing entries; `case_study` keys map to the 20 sections)
- Architecture diagrams: edit `data/architectures.json` (Mermaid) or add images to `assets/diagrams/`
- Resume: put `resume.pdf` in `assets/resume/`
- Notes/PDFs: add `.md` files under `projects/` or PDFs under `assets/`

Content rule: never present academic or conceptual work as production experience.
