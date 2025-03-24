import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Prompt for Terraform script generation
prompt = "Generate a Terraform script to deploy a Jenkins server on AWS."

# Get the response
response = model.generate_content(prompt)

# Extract generated content
terraform_script = response.text  

# Save the script to a file
with open("jenkins.tf", "w") as file:
    file.write(terraform_script)

print("Terraform script generated successfully!")
