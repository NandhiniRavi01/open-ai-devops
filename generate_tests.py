import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Python function to generate test cases for
code_snippet = """
def add(a, b):
    return a + b
"""

# Prompt for AI
prompt = f"Generate Python unit test cases using unittest module for the following function:\n{code_snippet}"

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

# Generate AI response
response = model.generate_content(prompt)

# Save the generated test cases
with open("test_cases.py", "w") as file:
    file.write(response.text)  # Saves the AI-generated test cases

print("Test cases generated successfully!")
