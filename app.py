from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello from flask!"

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))  # default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
