from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Awaaz AI backend running on Render"
@app.route("/webhook", methods = ["POST"])
def telegram_webhook():
    data = request.get_json()
    print(data)
    return "OK", 200
