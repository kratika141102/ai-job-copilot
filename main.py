from fastapi import FastAPI, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from resume import extract_text_from_pdf
from skill_extractor import extract_skills
from resume_improver import generate_resume_suggestions
from ai_analyzer import analyze_with_ai
from interview_generator import generate_interview_questions
from answer_evaluator import evaluate_answer


app = FastAPI(title="AI Job Copilot")


# ==========================================
# STATIC FRONTEND
# ==========================================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# ==========================================
# HOME / FRONTEND
# ==========================================

@app.get("/")
def home():

    return FileResponse("static/index.html")


# ==========================================
# ANALYZE RESUME
# ==========================================

@app.post("/analyze-resume")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    # --------------------------------------
    # 1. Save uploaded resume
    # --------------------------------------

    file_path = "resume.pdf"

    with open(file_path, "wb") as buffer:

        buffer.write(await file.read())


    # --------------------------------------
    # 2. Extract resume text
    # --------------------------------------

    resume_text = extract_text_from_pdf(file_path)


    # --------------------------------------
    # 3. Extract resume skills
    # --------------------------------------

    resume_skills = extract_skills(resume_text)


    # --------------------------------------
    # 4. Extract job skills
    # --------------------------------------

    job_skills = extract_skills(job_description)


    # --------------------------------------
    # 5. Matched skills
    # --------------------------------------

    matched_skills = []

    for skill in job_skills:

        if skill in resume_skills:

            matched_skills.append(skill)


    # --------------------------------------
    # 6. Missing skills
    # --------------------------------------

    missing_skills = []

    for skill in job_skills:

        if skill not in resume_skills:

            missing_skills.append(skill)


    # --------------------------------------
    # 7. Match score
    # --------------------------------------

    if len(job_skills) > 0:

        match_score = round(
            (len(matched_skills) / len(job_skills)) * 100
        )

    else:

        match_score = 0


    # --------------------------------------
    # 8. Recommendations
    # --------------------------------------

    recommendation_map = {

        "Python":
            "Revise Python basics, OOP, functions and exception handling.",

        "SQL":
            "Practice SQL queries, joins, subqueries and database operations.",

        "PostgreSQL":
            "Learn PostgreSQL basics, tables, queries, joins and Python integration.",

        "FastAPI":
            "Learn FastAPI routing, request/response handling, Pydantic and CRUD APIs.",

        "REST API":
            "Learn HTTP methods, status codes, JSON, endpoints and REST API design.",

        "Docker":
            "Learn Docker images, containers, Dockerfile and basic deployment.",

        "Git":
            "Practice Git add, commit, push, pull and branching.",

        "GitHub":
            "Practice repositories, branches, pull requests and GitHub workflow.",

        "OOP":
            "Revise classes, objects, inheritance, encapsulation and polymorphism."
    }


    recommendations = []

    for skill in missing_skills:

        recommendation = recommendation_map.get(
            skill,
            f"Learn and practice {skill}."
        )

        recommendations.append({

            "skill": skill,

            "recommendation": recommendation
        })


    # --------------------------------------
    # 9. Resume suggestions
    # --------------------------------------

    resume_suggestions = generate_resume_suggestions(

        resume_skills,

        job_skills,

        missing_skills
    )


    # --------------------------------------
    # 10. AI analysis
    # --------------------------------------

    ai_analysis = analyze_with_ai(

        resume_text,

        job_description
    )


    # --------------------------------------
    # 11. AI interview questions
    # --------------------------------------

    interview_questions = generate_interview_questions(

        resume_text,

        job_description
    )


    # --------------------------------------
    # 12. Return result
    # --------------------------------------

    return {

        "filename": file.filename,

        "resume_skills": resume_skills,

        "job_required_skills": job_skills,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "match_score": match_score,

        "recommendations": recommendations,

        "resume_suggestions": resume_suggestions,

        "ai_analysis": ai_analysis,

        "interview_questions": interview_questions
    }


# ==========================================
# AI ANSWER EVALUATOR
# ==========================================

@app.post("/evaluate-answer")
async def evaluate_interview_answer(
    question: str = Form(...),
    user_answer: str = Form(...)
):

    result = evaluate_answer(

        question,

        user_answer
    )


    return {

        "question": question,

        "user_answer": user_answer,

        "evaluation": result
    }