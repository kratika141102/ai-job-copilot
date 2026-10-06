
from answer_evaluator import evaluate_answer


question = "What is OOP in Python?"

user_answer = """
OOP means Object Oriented Programming.
It is a programming approach based on classes and objects.
It helps organize code and make it reusable.
"""


result = evaluate_answer(
    question,
    user_answer
)

print(result)