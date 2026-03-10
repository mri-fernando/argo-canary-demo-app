from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from version 6"

@app.route("/health")
def health():
    return "ok"

@app.route("/error")
def error():
    if random.random() < 0.3:
        return "error", 500
    return "ok"
    
app.run(host="0.0.0.0", port=5000)