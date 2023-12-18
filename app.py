from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__, template_folder='templates')
CORS(app)
# Set up OpenAI API credentials
openai.api_key = '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'


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
#
#
#
#
#
#
#
#
# # Define the /api route to handle POST requests
# @app.route("/api", methods=["POST"])
# def api():
#
#     message = request.form.get("message")
# #prompt = input("ask me something")
#
# # Make an API call to ChatGPT
# response = openai.Completion.create(
#     engine="text-davinci-003",  # This engine is known for its versatility and high-quality responses
#     prompt= message,
#     #    messages=[
#     #       {"role": "system", "content": "You are a helpful assistant."},
#     #      {"role": "user", "content": "Hello!"}
#     # ],
#     max_tokens=150
# )

# print(completion.choices[0].message)

# Get the generated response
# chatgpt_response = response['choices'][0]['text']

# Print the response
# print(chatgpt_response)

#   message = request.form.get("message")
# completion = openai.chatCompletion.created(model="gpt-3.5-turbo", messages=[ {"role": "system", "content": "You are a helpful assistant."},
#       ]
#  )

# print(completion.choices[0].message.content)
# return completion.choices[0].message.content

# if __name__=='__main__':
#   app.run()
