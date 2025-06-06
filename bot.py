import os
import telebot
from flask import Flask, request

TOKEN = '7334013777:AAEQVcRi6MpiDok7_Tsl9JQSjPWYAxHSH-g'
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
    # ساخت متن با نام یا آیدی کاربر و متن پیام
    user_info = message.from_user.username or message.from_user.first_name or "ناشناس"
    text_to_send = f"پیام از کاربر {user_info}:\n{message.text}"
    
    # ارسال پیام به همان چت (صفحه ربات)
    bot.send_message(message.chat.id, text_to_send)
    
    # پاسخ دادن به کاربر
    bot.reply_to(message, "received")

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=f'https://my-telegram-bot-wi2v.onrender.com/{TOKEN}')
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
