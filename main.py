import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]
token_limit = 150
message = []

while token_limit > 0:
    now_input = input("Prompt: ")
    
    message.append({"role": "user", "content": now_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message
    )

    print(response.choices[0]["message"]["content"].strip())

    token_limit -= response["usage"]["total_tokens"]
    message.append(response.choices[0]["message"])

print("Thank you for using.")
