import requests
from flask import Flask, request

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "**********"
USER_ID="**********"


def send_line(message):

    url = "https://api.line.me/v2/bot/message/push"

    headers = {
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "to": USER_ID,
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }

    response = requests.post(url, headers=headers, json = data)
    print(response.status_code)

if __name__ == "__main__":
    app.run(port=5000)
