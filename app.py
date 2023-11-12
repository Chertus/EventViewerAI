from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_talisman import Talisman
from aichat import AIChatBot
import os

app = Flask(__name__)
CORS(app)
Talisman(app)

openai_api_key = os.getenv('OPENAI_API_KEY')
chatbot = AIChatBot('enriched_logs.json', openai_api_key)

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    answer = chatbot.ask_question(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
