import telebot
from decouple import config
import requests

bot_token = config("token_key")

bot = telebot.TeleBot(bot_token)

greetings = ["hey", "hi", "hello", "how are you"]
activity = ["activity"]
joke=["joke","jokes"]




def getActivity():
    URL = "https://www.boredapi.com/api/activity"
    response = requests.get(URL)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        report = data['activity']
        return report
    else:
        print("Error in the HTTP request")

def getJoke():
    URL2 = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(URL2)
    if response.status_code == 200:
        data = response.json()
        setup = data['setup']
        punchline=data['punchline']
        return setup + punchline
    else:
        print("Error in the HTTP request")




@bot.message_handler(commands=["start", "help"])
def welcome(message):
    bot.send_message(message.chat.id, "WELCOME TO K3LIIL")

def isMsg(message):
    return True

@bot.message_handler(func=isMsg)
def reply(message):
    words = message.text.split()

    if words[0].lower() in joke :
        ri=getJoke()
        return bot.send_message(message.chat.id,ri)
    if words[0].lower() in activity:
        report = getActivity()  
        return bot.send_message(message.chat.id, report)
    if words[0].lower() in greetings:
        bot.reply_to(message, "how are you")
    else:
        bot.reply_to(message, "this is not a command")

bot.polling()

