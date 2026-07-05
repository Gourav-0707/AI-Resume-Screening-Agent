import re

SKILLS = [
    "Python",
    "Java",
    "C++",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "FastAPI",
    "Docker",
    "Git",
    "REST API",
    "LangChain",
    "RAG",
    "OpenAI",
    "LLM",
    "TensorFlow",
    "PyTorch",
    "Pandas",
    "NumPy",
    "Scikit-learn"
]

def extract_skills(text):
    found_skills = []

    text = text.lower()

    for skill in SKILLS:
        if re.search(r"\b" + re.escape(skill.lower()) + r"\b", text):
            found_skills.append(skill)

    return sorted(found_skills)