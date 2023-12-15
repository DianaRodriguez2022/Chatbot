import completion as completion
from flask import Flask, render_template, request
import openai
from openai import OpenAI

import os

app = Flask(__name__)
openai.api_key = 'API KEY'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/main', methods=['POST'])
def main():
    # Get user message from the request
    user_message = request.form['message']

    # send mesage  to OPENAI's Api and receive the response
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        stream=True
    )

    print(completion.choices[0].message)