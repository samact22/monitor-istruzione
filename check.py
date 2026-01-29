import requests
import os

# ================= CONFIG =================
URL = "https://www.istruzione.it/manutenzione/index.html"

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

STATE_FILE = "state.txt"
# =========================================

def send_telegram(message):
    api = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(api, data={"chat_id": CHAT_ID, "text": message})
    except Exception as e:
        print("Errore invio Telegram:", e)

def get_state():
    if os.path.exists(STATE_FILE):
        return open(STATE_FILE, "r").read().strip()
    return None

def save_state(state):
    open(STATE_FILE, "w").write(state)

# Controllo sito
try:
    r = requests.get(URL, timeout=10)
    r.raise_for_status()
    text = r.text.lower()
    if "manutenzione" in text:
        current_state = "offline"
    else:
        current_state = "online"
except Exception:
    current_state = "offline"

previous_state = get_state()

if current_state != previous_state:
    if current_state == "online":
        send_telegram(f"✅ istruzione.it ONLINE!\n{URL}")
    else:
        send_telegram(f"⚠️ istruzione.it IN MANUTENZIONE\n{URL}")
    save_state(current_state)
else:
    print(f"✔ Stato invariato: {current_state}")

