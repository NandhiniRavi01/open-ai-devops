import openai  

openai.api_key = "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"  # Replace with your OpenAI API key

code_snippet = """
def add(a, b):
    return a + b
"""

prompt = f"Generate Python test cases for the following function:\n{code_snippet}"

response = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=[{"role": "user", "content": prompt}]
)

test_cases = response['choices'][0]['message']['content']

with open("test_cases.py", "w") as file:
    file.write(test_cases)  # Saves the AI-generated test cases

print("Test cases generated successfully!")

