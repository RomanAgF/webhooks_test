import requests
from flask import Flask, request

app = Flask(__name__)

# Вставь сюда свой токен Telegram
TELEGRAM_BOT_TOKEN = '7201807860:AAFrdTVZaZfNNUWi70SV1mKibsItmveEItQ'
TELEGRAM_CHAT_ID = '352566109'

def send_message_to_telegram(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {'chat_id': TELEGRAM_CHAT_ID, 'text': text}
    response = requests.post(url, data=data)
    return response

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    task_title = data['data']['FIELDS']['TITLE']  # Пример: берем название задачи
    message = f'Новая задача создана: {task_title}'
    send_message_to_telegram(message)
    return 'OK', 200

# Добавление обработки корневого маршрута
@app.route('/')
def index():
    return 'Webhook is active. Please send data to /webhook endpoint.', 200

# app.run() не нужен для развертывания на Vercel, его можно удалить
