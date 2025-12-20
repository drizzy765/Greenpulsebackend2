import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
print(f"API Key present: {bool(api_key)}")
if api_key:
    print(f"Key starts with: {api_key[:4]}...")

client = Groq(api_key=api_key)

try:
    print("Sending request to Groq...")
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain the importance of low latency LLMs",
            }
        ],
        model="llama-3.1-8b-instant",
    )
    print("Success!")
    print(completion.choices[0].message.content[:100])
except Exception as e:
    print(f"Error: {e}")
