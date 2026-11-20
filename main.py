
import os
import re
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

KEYWORDS = [
    "ракетна небезпека",
    "ракетна загроза",
    "балістична загроза",
    "загроза застосування ракет",
    "ракетная опасность",
    "ракетная угроза"
]

def should_send(message):
    text = message.lower()
    if not any(word in text for word in KEYWORDS):
        return False

    drone_only = [
        "шахед", "shahed", "бпла",
        "безпілотник", "дрон"
    ]

    if any(word in text for word in drone_only):
        return False

    return True

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    }, timeout=15)
