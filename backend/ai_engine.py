from openai import OpenAI
from knowledge_base import COVELNT_DATA
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def reply(q, context=""):
    prompt = f"""
You are Fantum Support, Covelnt’s AI assistant.

Rules:
- Answer ONLY based on given company data
- Be friendly and short
- If unsure, say "Please contact support@covelnt.com"

Company info:
{COVELNT_DATA}

User uploaded content:
{context}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": q}
            ],
            temperature=0.4
        )

        return response.choices[0].message.content

    except Exception as e:
        print("OPENAI ERROR:", e)
        return str(e)

