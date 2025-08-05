import telebot
from config import BOT_TOKEN
from joi_core import generate_reply

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.first_name
    bot.send_message(message.chat.id, f"👋 Hello {user}, I’m Joi — your companion in code and silence.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    reply = generate_reply(msg)
    bot.send_message(message.chat.id, reply)

bot.infinity_polling()
