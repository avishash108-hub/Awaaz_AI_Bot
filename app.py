from flask import Flask, request
import os
import requests
from google.cloud import dialogflow_v2 as dialogflow
import json
from google.oauth2 import service_account
credentials_info = json.loads(
    os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")
)

credentials = service_account.Credentials.from_service_account_info(
    credentials_info
)

app = Flask(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
PROJECT_ID = os.environ.get("DIALOGFLOW_PROJECT_ID")

def detect_intent_texts(text, session_id, language_code="en"):
    session_client = dialogflow.SessionsClient(credentials=credentials)


    session = session_client.session_path(PROJECT_ID , session_id)

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
@app.route("/webhook", methods=["POST"])
def telegram_webhook():
    data = request.get_json()

    if "message" not in data:
        return "", 200

    chat_id = data["message"]["chat"]["id"]
    text_received = data["message"].get("text", "")

    reply = detect_intent_texts(text_received, str(chat_id))
    send_message(chat_id, reply)

    return "", 200


    
def send_message(chat_id, reply):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id" : chat_id,
        "text" : reply
    }
    requests.post(url, json=payload)
    









