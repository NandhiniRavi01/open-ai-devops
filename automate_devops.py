import openai  

openai.api_key = "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"  # Replace with your OpenAI API key

prompt = "Generate a Terraform script to deploy a Jenkins server on AWS."

response = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=[{"role": "user", "content": prompt}]
)

terraform_script = response['choices'][0]['message']['content']

with open("jenkins.tf", "w") as file:
    file.write(terraform_script)  # Saves the generated Terraform script

print("Terraform script generated successfully!")

