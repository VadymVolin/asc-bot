import os
import telebot

API_KEY = os.getenv('API_KEY')

bot = telebot.AsyncTeleBot(API_KEY)

print(bot.get_me())

@bot.message_handler(commands=['start'])
def startCmd(message):
    bot.reply_to(message, "Hey, let's start")


bot.polling(non_stop=True)
