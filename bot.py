import os
import telebot
from flask import Flask, request

TOKEN = '7334013777:AAFSZ7ITYkxV-MR0z9NKWVcTxd9WzvA0z5Y'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return ''

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "recived")

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=f'https://my-telegram-bot_render.onrender.com/{TOKEN}')
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)




