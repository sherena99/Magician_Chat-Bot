from flask import Flask, render_template, request
import openai

openai.api_key = "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"  # Replace with OpenAI API secret key

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    return get_Chat_response(msg)

def get_Chat_response(text):
    input_data = [text]

    input_ids = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_data,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    ).choices[0].text.strip()

    return input_ids

if __name__ == '__main__':
    app.run()
