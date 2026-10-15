# ResumeLens AI 🔎

ResumeLens AI is an original, lightweight resume-review app that compares a text-based PDF resume with a job description. It highlights text overlap, detects skills from a transparent built-in dictionary, and offers practical prompts for tailoring an application.

> **Important:** The similarity percentage is a simple TF-IDF/cosine-similarity heuristic. It is not an official ATS score, does not reproduce any employer's screening system, and cannot predict hiring outcomes.

## Features

- Extract selectable text from PDF resumes
- Compare resume text with a pasted job description
- Show a heuristic text-similarity percentage and word counts
- Identify detected shared skills and potential gaps
- Download a plain-text analysis report
- Run basic unit tests with GitHub Actions

## Tech stack

- Python
- Streamlit
- pypdf
- scikit-learn (TF-IDF and cosine similarity)
- unittest and GitHub Actions

## Run locally

Python 3.10+ is recommended.

```bash
git clone https://github.com/a-ayushguptaaa76/resume-lens-ai.git
cd resume-lens-ai
python -m venv .venv
```

Activate the environment:

- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Install and launch:

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Streamlit will print a local URL, usually `http://localhost:8501`.

## Tests

```bash
python -m unittest discover -s tests -v
```

## How the analysis works

1. **PDF parsing:** extracts selectable text from each page. Scanned image-only PDFs may need OCR and are not supported by the current MVP.
2. **Text similarity:** TF-IDF vectorization with unigram and bigram features is used to calculate cosine similarity between the resume and job description.
3. **Skill detection:** a small, readable dictionary finds known technical and business skills.
4. **Feedback:** the app lists detected matches and gaps for the user to review.

The similarity value is not a probability. Results vary with wording, document structure, and the skill dictionary. A missing skill is only a prompt to review the job description—not a recommendation to claim experience you do not have.

## Privacy

This project does not intentionally save uploaded resumes to a database or disk; processing happens in the app session. When deploying the app, review the hosting provider's data handling, logging, and retention policies before uploading sensitive documents.

## Roadmap

- [ ] Add OCR support for scanned PDFs
- [ ] Improve skill aliases and role-specific dictionaries
- [ ] Add section detection and resume completeness checks
- [ ] Add more parser and edge-case tests
- [ ] Deploy a public demo

## Responsible use

Use the output as an editing aid. Keep every skill, qualification, and achievement truthful, and review suggestions manually before sending an application.

## License

This project is currently provided without an explicit open-source license. Add a license file if you want to grant others specific reuse permissions.
