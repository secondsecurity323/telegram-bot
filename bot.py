import os
import telebot
from flask import Flask, request

TOKEN = '7334013777:AAEQVcRi6MpiDok7_Tsl9JQSjPWYAxHSH-g'
OWNER_CHAT_ID = 1656844563

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return ''

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # ارسال پیام "received" به کاربر
    bot.reply_to(message, "received")

    # ساخت پیام برای ارسال به خودت (صاحب ربات)
    user_info = message.from_user.username or message.from_user.first_name or "ناشناس"
    text_for_owner = f"پیام از کاربر {user_info} (id={message.from_user.id}):\n{message.text}"

    # ارسال پیام به چت خودت
    bot.send_message(OWNER_CHAT_ID, text_for_owner)

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=f'https://my-telegram-bot-wi2v.onrender.com/{TOKEN}')
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
