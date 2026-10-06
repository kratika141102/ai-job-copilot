
import ollama


def evaluate_answer(question, user_answer):

    prompt = f"""
You are an expert technical interviewer evaluating a fresher.

Evaluate the candidate's answer to the interview question.

IMPORTANT RULES:
- Evaluate ONLY the answer provided.
- Do not assume experience that is not mentioned.
- Do not invent projects, skills, or achievements.
- Be fair to a fresher.
- Give practical feedback.
- Score the answer from 0 to 10.

INTERVIEW QUESTION:
{question}

CANDIDATE ANSWER:
{user_answer}

Return the result in exactly this format:

### Score
Give a score out of 10.

### Strengths
List 2-3 things the candidate did well.

### Mistakes
List important mistakes or missing points.
If there are no major mistakes, say "No major mistakes."

### Improved Answer
Give a simple, interview-ready answer that the candidate
could give.

### Interview Verdict
Give one short sentence:
Excellent / Good / Needs Improvement / Weak

Keep the explanation suitable for a fresher.
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
