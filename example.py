from flask import Flask
from threading import Thread
import os
import time
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "Bot is running"

def run():
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def self_ping():
    url = os.getenv("SELF_URL") 
    if not url:
        print("SELF_URL not set, self-ping disabled")
        return
    while True:
        try:
            requests.get(url)
        except:
            pass
        time.sleep(600)  # Ping every 10 minutes

def example():
    t = Thread(target=run)
    t.daemon = True
    t.start()

    ping_thread = Thread(target=self_ping)
    ping_thread.daemon = True
    ping_thread.start()
