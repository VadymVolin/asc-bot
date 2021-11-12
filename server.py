import os

import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.AsyncTeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def startCmd(message):
    bot.reply_to(message, "Hey, let's start")


# @bot.message_handler(func=lambda message: True)
# def handleMessage(message):
#     bot.reply_to(message, message.text)

# Handles all messages which text matches regexp.
# @bot.message_handler(regexp='someregexp')
# def command_help(message):
#     bot.send_message(message.chat.id, 'Did someone call for help?')

@bot.message_handler(chat_types=['private'])
def command_help(message):
    message_text = message.text
    print("Received private chat message: ", message_text)
    result_text = "Received private chat message " \
                  + message.from_user.first_name \
                  + "(@" + message.from_user.username \
                  + "): [" + message_text + "]. Thank you!"
    bot.send_message(message.chat.id, result_text)


# Handle all sent documents of type 'text/plain'.


# @bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
# def command_handle_document(message):
#     print("Received doc message", message)
#     bot.send_message(message.chat.id, 'Document received, sir!')

# Handle all other messages.


@bot.message_handler(func=lambda message: True, content_types=['text'])
def default_command(message):
    message_text = message.text
    print("Received text message: ", message_text)
    result_text = "Received text message from " + message.from_user.first_name + \
                  "(@" + message.from_user.username + \
                  "): [" + message_text + "]. Thank you!"
    bot.send_message(message.chat.id, result_text)


# Handle all other messages.


@bot.message_handler(func=lambda message: True, chat_types=['private', 'group', 'supergroup', 'channel'], content_types=['photo', 'sticker'])
def receive_img(message):
    message_text = message.text
    print("Received text message: ", message_text)
    print( message.from_user.first_name)
    result_text = "Received text message from " + message.from_user.first_name + \
                  "(@" + message.from_user.username + \
                  "): [" + message.sticker.emoji + "]. Thank you!"
    bot.send_message(message.chat.id, result_text)


# @bot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
# def default_command(message):
#     bot.send_message(message.chat.id, "This is the default command handler.")


bot.infinity_polling()
