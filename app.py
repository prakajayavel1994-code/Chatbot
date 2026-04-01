from flask import Flask, request, jsonify, send_from_directory
import requests
import json
import os

app = Flask(__name__)

FILE = "history.json"

def load():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    return {}
                return data
            except:
                return {}
    return {}

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    msg = data['message']
    chat_id = data['chat_id']

    db = load()

    if chat_id not in db:
        db[chat_id] = []

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "tinyllama",
                "prompt": msg,
                "stream": False
            }
        )

        reply = response.json().get("response", "No reply")

        db[chat_id].append({"user": msg, "bot": reply})
        save(db)

        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"response": "Error: " + str(e)})

@app.route('/get_chats')
def get_chats():
    return jsonify(list(load().keys()))

@app.route('/get_chat/<chat_id>')
def get_chat(chat_id):
    return jsonify(load().get(chat_id, []))

if __name__ == "__main__":
    app.run(debug=True)