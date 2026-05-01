import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("google/flan-t5-large")

def generate_answer(context, query):
    prompt = f"""
Answer the question using the emails below.

Emails:
{context}

Question:
{query}

Answer in bullet points:
"""

    response = model.generate_content(prompt)
    return response.text