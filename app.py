from flask import Flask, request
import os
import requests
from google.cloud import dialogflow_v2 as dialogflow

app = Flask(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
PROJECT_ID = os.environ.get("DIALOGFLOW_PROJECT_ID")

def detect_intent_texts(project_id, session_id, text, language_code="en"):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(
        text=text,
        language_code=language_code
    )

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={
            "session": session,
            "query_input": query_input
        }
    )

    return response.query_result.fulfillment_text

@app.route("/")
def home():
    return "Awaaz AI backend running on Render"
@app.route("/webhook", methods = ["POST"])
def telegram_webhook():
    data = request.get_json()
    chat_id = data["message"]["chat"]["id"]
    text_received = data["message"].get("text", "")
     

session_id = str(chat_id)

reply = detect_intent_texts(
    PROJECT_ID,
    session_id,
    user_text
)
    send_message(chat_id, reply)
    return "OK", 200

    
def send_message(chat_id, reply):
    url = f"https://api.telegram.org/bot7673865028:AAE4uebFECz0y7Gzg_7tB1KWLNzcPwKBw4g/sendMessage"
    payload = {
        "chat_id" : chat_id,
        "text" : reply
    }
    requests.post(url, json=payload)
    







