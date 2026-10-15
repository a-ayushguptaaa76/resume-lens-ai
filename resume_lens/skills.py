import re

# A deliberately small, transparent dictionary. Extend it for your target roles.
SKILL_TERMS = {
    "python", "java", "c++", "sql", "javascript", "typescript", "html", "css",
    "react", "node.js", "flask", "django", "streamlit", "rest api", "git", "github",
    "linux", "docker", "kubernetes", "aws", "azure", "gcp", "ci/cd", "jenkins",
    "machine learning", "deep learning", "natural language processing", "nlp",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "power bi",
    "excel", "tableau", "communication", "project management", "sales", "negotiation",
    "lead generation", "customer relationship management", "crm", "market research",
    "business development", "account management", "cold calling",
}


def find_skills(text: str) -> set[str]:
    """Find known skill phrases using case-insensitive whole-phrase matching."""
    lowered = text.lower()
    found = set()
    for skill in SKILL_TERMS:
        pattern = r"(?<![\w+#])" + re.escape(skill) + r"(?![\w+#])"
        if re.search(pattern, lowered):
            found.add(skill)
    return found
