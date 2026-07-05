import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env")

client = Groq(api_key=API_KEY)


def extract_skills(resume_text):
    prompt = f"""
You are an ATS Resume Parser.

Extract ONLY technical skills from the following resume.

Return ONLY a JSON array.

Example:

[
    "Python",
    "Django",
    "React",
    "PostgreSQL",
    "Docker",
    "Git"
]

Resume:
{resume_text}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        text = response.choices[0].message.content.strip()

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        print("Groq Response:")
        print(text)

        return json.loads(text)

    except Exception as e:
        print("Groq Error:", e)
        return []


def generate_interview_questions(role, level, skills):
    prompt = f"""
Generate 10 interview questions.

Role: {role}

Difficulty: {level}

Skills: {skills}

Return ONLY JSON.

Example:

[
    {{
        "question":"Explain Django ORM."
    }},
    {{
        "question":"What is JWT Authentication?"
    }}
]
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5
        )

        text = response.choices[0].message.content.strip()

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        return json.loads(text)

    except Exception as e:
        print("Groq Error:", e)
        return []


def evaluate_answer(question, answer):
    prompt = f"""
Evaluate the following interview answer.

Question:
{question}

Answer:
{answer}

Return ONLY JSON.

Example:

{{
    "score": 8,
    "feedback": "Good answer, but explain JWT expiration.",
    "correct_answer": "JWT is..."
}}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        text = response.choices[0].message.content.strip()

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        return json.loads(text)

    except Exception as e:
        print("Groq Error:", e)
        return {
            "score": 0,
            "feedback": "Unable to evaluate answer.",
            "correct_answer": ""
        }