import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_TOKEN = '7201807860:AAFrdTVZaZfNNUWi70SV1mKibsItmveEItQ'
CHAT_ID = '352566109'


def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Здесь можно обрабатывать данные и формировать сообщение
    send_message(f"Новое событие: {data}")
    return 'OK'


if __name__ == '__main__':
    app.run(port=5000)