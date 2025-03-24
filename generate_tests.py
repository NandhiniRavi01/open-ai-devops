import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in the environment variables.")

genai.configure(api_key=api_key)

# Python function to generate test cases for
code_snippet = """
def add(a, b):
    return a + b
"""

# Prompt for AI
prompt = f"Generate Python unit test cases using unittest module for the following function:\n{code_snippet}"

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Generate AI response
try:
    response = model.generate_content(prompt)
    # Save the generated test cases
    with open("test_cases.py", "w") as file:
        file.write(response.text)  # Saves the AI-generated test cases
    print("Test cases generated successfully!")
except Exception as e:
    print(f"Error generating test cases: {e}")
