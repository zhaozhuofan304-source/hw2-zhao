import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set.")

client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = """
You are a customer support assistant for a small online retail company.
Write a professional first-draft email reply in English.

Rules:
- Be polite, clear, and concise.
- Do not make up order details, refund status, tracking numbers, or company policies.
- Ask for missing information if needed.
- If the case involves threats, fraud claims, or sensitive escalation, recommend human review.
""".strip()

user_input = input("Enter message: ")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]
)

print("\nAI reply:\n")
print(response.choices[0].message.content)
