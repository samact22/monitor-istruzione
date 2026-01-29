import requests
import os

URL = "https://www.istruzione.it/manutenzione/index.html"

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send(msg):
    api = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(api, data={"chat_id": CHAT_ID, "text": msg})

r = requests.get(URL, timeout=10)
text = r.text.lower()

if "manutenzione" not in text:
    send("✅ istruzione.it ONLINE!\nhttps://www.istruzione.it")
