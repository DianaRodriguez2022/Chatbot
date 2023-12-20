from flask import Flask, render_template, request, jsonify
import openai
import json

app = Flask(__name__, template_folder='templates')
# train chatbot
train = json.loads(open('venv/train.json').read())

# Set up OpenAI API credentials
openai.api_key = 'API Key'

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

@app.route('/api', methods=['POST'])
def ask_chatbot(user_input):
    prompt = f"User: {user_input}\nChatbot:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        n=1,
        stop=None
    )

    chatbot_reply = response['choices'][0]['text'].strip()

    return chatbot_reply


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    chatbot_response = ask_chatbot(user_input)
    return jsonify({'response': chatbot_response})


if __name__ == '__main__':
    app.run()
