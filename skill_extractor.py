import re


SKILL_PATTERNS = [
    "Python",
    "Java",
    "C++",
    "C#",
    "JavaScript",
    "TypeScript",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "SQLite",
    "MongoDB",
    "FastAPI",
    "Django",
    "Flask",
    "REST API",
    "React",
    "Angular",
    "HTML",
    "CSS",
    "Node.js",
    "Git",
    "GitHub",
    "Docker",
    "Kubernetes",
    "AWS",
    "Azure",
    "Pandas",
    "NumPy",
    "TensorFlow",
    "PyTorch",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "Generative AI",
    "LangChain",
    "RAG",
    "OOP",
    "CRUD",
    "Tkinter",
    "Pygame",
    "Linux",
    "Pytest"
]


def extract_skills(text):

    found_skills = []

    text_lower = text.lower()

    for skill in SKILL_PATTERNS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return found_skills