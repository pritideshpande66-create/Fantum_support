import requests
import os
from dotenv import load_dotenv
from knowledge_base import COVELNT_DATA

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def reply(q, context=""):

    prompt = f"""
You are Fantum Support, Covelnt’s AI assistant.

Rules:
Rules:
- Answer ONLY based on company data
- Be friendly and short
- Reply in the SAME language as the user
- If user writes Hindi in English letters (Hinglish), reply in Hindi
- If unsure say "Please contact support@covelnt.com"

Company info:
{COVELNT_DATA}

User uploaded content:
{context}

User question:
{q}
"""

    try:

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek/deepseek-chat",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        data = response.json()
        print(response)

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("AI ERROR:", e)
        return "AI error occurred"


