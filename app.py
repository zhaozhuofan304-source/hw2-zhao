import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

user_input = input("Enter message: ")

response = model.generate_content(user_input)

print("\nAI reply:\n")
print(response.text)
