from dotenv import load_dotenv, find_dotenv
import os

print(f"Loading env from: {find_dotenv()}")
load_dotenv(find_dotenv())

key = os.getenv("GROQ_API_KEY")
print(f"GROQ_API_KEY exists: {bool(key)}")
if key:
    print(f"Key starts with: {key[:5]}...")
    print(f"Key ends with: ...{key[-5:]}")
else:
    print("GROQ_API_KEY is NOT set.")
