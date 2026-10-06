from ai_analyzer import analyze_with_ai


resume = """
Python developer fresher.
Skills: Python, SQL, SQLite, Git, GitHub, OOP.
"""

job = """
Looking for a Python developer with Python,
SQL, FastAPI, Docker and PostgreSQL.
"""


result = analyze_with_ai(resume, job)

print(result)