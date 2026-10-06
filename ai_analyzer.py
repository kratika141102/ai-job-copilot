import ollama


def analyze_with_ai(resume_text, job_description):

    prompt = f"""
You are an expert technical recruiter.

Analyze the resume against the job description.

IMPORTANT RULES:
- Use ONLY information explicitly present in the resume.
- NEVER invent skills, projects, experience, achievements, education,
  communication skills, or technologies.
- If a skill is mentioned in the job description but NOT in the resume,
  clearly say it is missing.
- Do not claim that the candidate has experience with a missing skill.
- Do not assume that the candidate has used a technology just because
  it appears in the job description.
- The candidate is a fresher, so keep recommendations realistic.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Provide a concise analysis with exactly these sections:

### Candidate Strengths
Mention only skills, projects, education, or achievements actually
present in the resume.

### Missing Skills
List technologies or skills required by the job description that are
not clearly present in the resume.

### Resume Improvement Suggestions
Suggest what the candidate can improve. Do not say the candidate
already knows a missing skill.

### Interview Preparation Topics
Suggest topics based on the job description and the candidate's
actual background.

### Overall Recommendation
Give an honest fresher-level assessment.

Remember:
DO NOT invent information.
DO NOT claim missing skills as existing skills.
"""

    # Connect to Ollama running on the Windows host
    client = ollama.Client(
        host="http://host.docker.internal:11434"
    )

    response = client.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
