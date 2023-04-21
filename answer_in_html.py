import os
import openai
import markdown
from bottle import route, run
import webbrowser

openai.api_key = os.environ["OPENAI_API_KEY"]
md = markdown.Markdown(extensions=["codehilite", "meta", "extra"])


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Output in MarkDown"},    
        {"role": "user", "content": "Print Hello World in Python Fast API"},
    ],
)

@route('/')
def home():
    return md.convert(response.choices[0]["message"]["content"].strip())

webbrowser.open("http://localhost:5000/", autoraise=True)

run(host='localhost', port=5000)
