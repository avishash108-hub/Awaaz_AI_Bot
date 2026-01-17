from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Awaaz AI backend running on Render"
@app.route("/webhook", methods = ["POST"])
def telegram_webhook():
    data = request.get_json()
    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    reply = "Hello 👋 I am Awaaz. I'm here to help you."
    send_message(chat_id, reply)
    return "OK", 200

    
def send_messages(chat_id, text):
    url = f"https://api.telegram.org/bot7673865028:AAE4uebFECz0y7Gzg_7tB1KWLNzcPwKBw4g/sendMessage"
    payload = {
        "chat_id" : chat_id
        "text" : text
    }
    requests.post(url, json=payload)
    


