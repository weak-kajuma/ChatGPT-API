import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

text = input("Prompt: ")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": text},
    ],
)

print(response.choices[0]["message"]["content"].strip())