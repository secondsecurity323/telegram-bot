import telebot
from flask import Flask, request

TOKEN = '7334013777:AAG4VlYzbCNB9L1vYpi5MG32EMFg2lNO1sM'
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
    bot.reply_to(message, "پیامت دریافت شد.")

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url='https://your-app-name.onrender.com/' + TOKEN)
    app.run(host='0.0.0.0', port=5000)
