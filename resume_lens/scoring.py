import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def _words(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z][a-zA-Z+#.\-]{1,}", text.lower()))


def compare_texts(resume_text: str, job_description: str) -> dict[str, int | float]:
    """Return heuristic text similarity and simple overlap statistics."""
    resume_text = resume_text.strip()
    job_description = job_description.strip()
    if not resume_text or not job_description:
        raise ValueError("Resume text and job description must both contain text.")

    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    matrix = vectorizer.fit_transform([resume_text, job_description])
    similarity = float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0])
    shared = _words(resume_text) & _words(job_description)
    return {
        "similarity": max(0.0, min(1.0, similarity)),
        "resume_words": len(resume_text.split()),
        "job_words": len(job_description.split()),
        "shared_terms": len(shared),
    }


def build_report(result: dict, matched_skills: list[str], missing_skills: list[str]) -> str:
    """Format a plain-text report for downloading."""
    return "\n".join([
        "RESUMELENS AI — RESUME REVIEW",
        "=" * 34,
        f"Heuristic text similarity: {result['similarity']:.1%}",
        f"Resume word count: {result['resume_words']}",
        f"Job description word count: {result['job_words']}",
        f"Shared unique terms: {result['shared_terms']}",
        "",
        "Matched skills:",
        ", ".join(matched_skills) or "None detected",
        "",
        "Potential skill gaps (review for relevance):",
        ", ".join(missing_skills) or "None detected",
        "",
        "Important: This is a lightweight heuristic, not an official ATS score.",
        "Only include skills and achievements that accurately represent your experience.",
    ])
