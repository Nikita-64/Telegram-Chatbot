from flask import Flask
from threading import Thread
import os

app = Flask(__name__)


@app.route("/")
def index():
    return "Bot is running"


def run():
    # Render provides PORT automatically
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)


def example():
    t = Thread(target=run)
    t.start()
