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

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام پیام تون رو بفرستید.")

def get_user_display(message):
    if message.from_user.id:
        return f"کاربر (ID: {message.from_user.id})"
    elif message.from_user.first_name:
        return f"کاربر ({message.from_user.first_name})"
    else:
        return "کاربر ناشناس"

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    user = get_user_display(message)

    # نوع پیام و متن یا فایلش رو تشخیص میدیم
    if message.text:
        content = message.text
        content_type = "متن"
    elif message.photo:
        content = "عکس ارسال شده"
        content_type = "عکس"
    elif message.video:
        content = "ویدیو ارسال شده"
        content_type = "ویدیو"
    elif message.sticker:
        content = f"استیکر ارسال شده - Emoji: {message.sticker.emoji}"
        content_type = "استیکر"
    elif message.animation:
        content = "گیف ارسال شده"
        content_type = "گیف"
    elif message.voice:
        content = "صدای ارسال شده"
        content_type = "صدا"
    else:
        content = "نوع پیام ناشناخته"
        content_type = "ناشناخته"

    # ساخت پیام برای ارسال به OWNER_CHAT_ID
    text_for_owner = f"پیام از {user}:\nنوع پیام: {content_type}\nمحتوا: {content}"

    try:
        bot.send_message(OWNER_CHAT_ID, text_for_owner)
    except Exception as e:
        print(f"خطا در ارسال پیام به صاحب بات: {e}")

    # پاسخ به کاربر
    bot.reply_to(message, "پیام شما دریافت شد.")

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=f'https://my-telegram-bot-wi2v.onrender.com/{TOKEN}')
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
