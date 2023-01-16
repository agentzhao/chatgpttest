from flask import Flask, jsonify, request
from chatgpt_wrapper import ChatGPT

app = Flask(__name__)
bot = ChatGPT()


@app.route("/chat", methods=["POST"])
def home():
    message = request.json["message"]
    response = bot.ask(message)
    return jsonify(response=response)


if __name__ == "__main__":
    app.run()
