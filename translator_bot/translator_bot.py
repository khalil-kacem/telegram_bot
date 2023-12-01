import telebot
from telebot import types, util
from decouple import config
from googletrans import Translator

BOT_TOKEN = config("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

trans = ["translate", "traduire", "traduction"]

@bot.message_handler(commands=["start", "help"])
def startBot(message):
    bot.send_message(message.chat.id, "Welcome to Daino!")

@bot.message_handler(func=lambda m: True)
def reply(message):
    words = message.text.split()
    if words[0] in trans:
        translator = Translator()
        translation = translator.translate(" ".join(words[1:]), dest="ar")
        bot.reply_to(message, translation.text)

bot.infinity_polling(allowed_updates=util.update_types)
