import requests
import os

# Settings
API_URL = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
LOG_FILE = "last_quake.txt"

def get_last_id():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return f.read().strip()
    return ""

try:
    response = requests.get(API_URL).json()
    data = response['Infogempa']['gempa']
    current_id = data['DateTime']

    if current_id != get_last_id():
        print("New earthquake detected!")
        # BMKG Shakemap image URL
        shakemap = f"https://data.bmkg.go.id/DataMKG/TEWS/{data['Shakemap']}"
        
        payload = {
            "embeds": [{
                "title": f"🚨 Gempa Terkini: M {data['Magnitude']}",
                "description": f"**Wilayah:** {data['Wilayah']}\n**Kedalaman:** {data['Kedalaman']}\n**Potensi:** {data['Potensi']}",
                "color": 15158332,
                "image": {"url": shakemap},
                "footer": {"text": f"Waktu: {data['Tanggal']} | {data['Jam']}"}
            }]
        }
        if WEBHOOK_URL:
            requests.post(WEBHOOK_URL, json=payload)

        if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
            tg_message = (
                f"🚨 *Gempa Terkini: M {data['Magnitude']}*\n"
                f"📍 *Wilayah:* {data['Wilayah']}\n"
                f"⬇️ *Kedalaman:* {data['Kedalaman']}\n"
                f"⚠️ *Potensi:* {data['Potensi']}\n"
                f"🕒 *Waktu:* {data['Tanggal']} | {data['Jam']}\n"
                f"[Peta Guncangan]({shakemap})"
            )
            tg_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            tg_payload = {
                "chat_id": TELEGRAM_CHAT_ID,
                "text": tg_message,
                "parse_mode": "Markdown"
            }
            requests.post(tg_url, json=tg_payload)

        # Update the local file for GitHub to commit
        with open(LOG_FILE, "w") as f:
            f.write(current_id)
    else:
        print("No new data.")
except Exception as e:
    print(f"Error: {e}")
