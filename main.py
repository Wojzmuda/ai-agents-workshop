import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
model = "gemini-2.5-flash"
user_input = sys.argv[1]
messages=[types.Content(
    role = "user",
    parts=[types.Part(text=user_input)],
)]


client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model=model,
    contents=messages,
)

print(response.text)