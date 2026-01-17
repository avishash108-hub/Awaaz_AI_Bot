from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Awaaz AI backend running on Render"
