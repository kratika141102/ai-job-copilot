def generate_resume_suggestions(
    resume_skills,
    job_skills,
    missing_skills
):
    suggestions = []

    # 1. Missing skills
    for skill in missing_skills:
        suggestions.append(
            f"Consider adding {skill} to your resume "
            f"after learning and practicing it."
        )

    # 2. Backend/API suggestion
    backend_skills = [
        "FastAPI",
        "Django",
        "Flask",
        "REST API"
    ]

    has_backend_skill = any(
        skill in resume_skills
        for skill in backend_skills
    )

    job_needs_backend = any(
        skill in job_skills
        for skill in backend_skills
    )

    if not has_backend_skill and job_needs_backend:
        suggestions.append(
            "Add backend or API project experience "
            "to strengthen your Python developer profile."
        )

    # 3. Database suggestion
    database_skills = [
        "SQL",
        "MySQL",
        "PostgreSQL",
        "SQLite",
        "MongoDB"
    ]

    has_database_skill = any(
        skill in resume_skills
        for skill in database_skills
    )

    if has_database_skill:
        suggestions.append(
            "Mention database operations, CRUD queries "
            "and database integration in your project descriptions."
        )

    # 4. Git/GitHub suggestion
    if "Git" in resume_skills and "GitHub" in resume_skills:
        suggestions.append(
            "Mention Git and GitHub usage clearly "
            "in your project descriptions."
        )

    # 5. Python suggestion
    if "Python" in resume_skills:
        suggestions.append(
            "Highlight your Python skills in your resume "
            "project descriptions and technical skills section."
        )

    return suggestions
