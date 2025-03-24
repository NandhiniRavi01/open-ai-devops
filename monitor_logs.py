import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Read Jenkins logs
with open("/var/log/jenkins/jenkins.log", "r") as log_file:
    logs = log_file.read()

# Define prompt for AI analysis
prompt = f"Analyze the following Jenkins logs and detect anomalies:\n{logs}"

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

# Get AI-generated response
response = model.generate_content(prompt)

print("AI-based log analysis result:")
print(response.text)
