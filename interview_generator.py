import ollama


def generate_interview_questions(resume_text, job_description):

    prompt = f"""
You are an expert technical interviewer.

Generate interview questions for a fresher candidate based ONLY
on the resume and job description provided below.

IMPORTANT RULES:

- Do not invent experience or skills.
- Do not assume the candidate knows something unless it appears
  in the resume or job description.
- Questions should be suitable for a fresher.
- Keep questions practical and interview-focused.
- Do not provide answers.
- Generate exactly 25 questions.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Generate exactly:

5 Python questions
5 SQL questions
5 Backend/API questions
5 Project-based questions
5 HR questions

Format the answer exactly like this:

### Python Questions

1. Question
2. Question
3. Question
4. Question
5. Question

### SQL Questions

1. Question
2. Question
3. Question
4. Question
5. Question

### Backend/API Questions

1. Question
2. Question
3. Question
4. Question
5. Question

### Project Questions

1. Question
2. Question
3. Question
4. Question
5. Question

### HR Questions

1. Question
2. Question
3. Question
4. Question
5. Question
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
