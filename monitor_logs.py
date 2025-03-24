import openai  

openai.api_key = "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"  # Replace with your OpenAI API key

# Read Jenkins logs
with open("/var/log/jenkins/jenkins.log", "r") as log_file:
    logs = log_file.read()

prompt = f"Analyze the following Jenkins logs and detect anomalies:\n{logs}"

response = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=[{"role": "user", "content": prompt}]
)

print("AI-based log analysis result:")
print(response['choices'][0]['message']['content'])

