import os
import telebot

from neuralink import start_learning
from image_matcher import check_image
from text_matcher import check_text
from config_constants import BASE_IMAGE_URL

API_KEY = os.getenv('API_KEY')
bot = telebot.AsyncTeleBot(API_KEY)


def notify_admins(chat_id, message):
    admins = bot.get_chat_administrators(chat_id).wait()
    for admin in admins:
        bot.send_message(admin.user.id, message)


@bot.message_handler(commands=['start'])
def startCmd(message):
    start_learning()
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
    check_image_result = False
    check_text_result = False
    invalid_text_segment = ''

    message_text = message.caption
    message_photo = message.photo
    message_sticker = message.sticker

    if message_text:
        check_text_result = check_text(message_text)

    if check_text_result:
        invalid_text_segment = "Text not valid"
        bot.delete_message(message.chat.id, message.message_id)
        result_text = "Received message with adult content from user: " + message.from_user.first_name + \
            "(@" + message.from_user.username + \
            "): [" + invalid_text_segment + \
                      "]. We notified admin's of the current chat."
        notify_admins(message.chat.id, result_text)

    if (not check_text_result) and message_photo:
        img_data = bot.get_file(message_photo[-1].file_id).wait()
        img_url = BASE_IMAGE_URL.format(API_KEY, img_data.file_path)
        check_image_result = check_image(img_url)

    if (not check_text_result) and message_sticker:
        img_data = bot.get_file(message_sticker.file_id).wait()
        img_url = BASE_IMAGE_URL.format(API_KEY, img_data.file_path)
        check_image_result = check_image(img_url)

    if check_image_result:
        bot.delete_message(message.chat.id, message.message_id)
        invalid_text_segment = "Media not valid"
        result_text = "Received message with adult content from user: " + message.from_user.first_name + \
            "(@" + message.from_user.username + \
            "): [" + invalid_text_segment + \
                      "]. We notified admin's of the current chat."
        notify_admins(message.chat.id, result_text)


# Handle all sent documents of type 'text/plain'.


# @bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
# def command_handle_document(message):
#     print("Received doc message", message)
#     bot.send_message(message.chat.id, 'Document received, sir!')

# Handle all other messages.


@bot.message_handler(func=lambda message: True, content_types=['text'])
def default_command(message):
    check_text_result = False
    invalid_text_segment = ''
    message_text = message.text
    if message_text:
        check_text_result = check_text(message_text)

    if check_text_result:
        invalid_text_segment = "Text not valid"
        bot.delete_message(message.chat.id, message.message_id)
        result_text = "Received message with adult content from user: " + message.from_user.first_name + \
            "(@" + message.from_user.username + \
            "): [" + invalid_text_segment + \
                      "]. We notified admin's of the current chat."
        notify_admins(message.chat.id, result_text)


# Handle all other messages.

@bot.message_handler(func=lambda message: True, content_types=['photo', 'sticker'])
def receive_img(message):
    check_image_result = False
    check_text_result = False
    invalid_text_segment = ''

    message_text = message.caption
    message_photo = message.photo
    message_sticker = message.sticker

    if message_text:
        check_text_result = check_text(message_text)

    if check_text_result:
        invalid_text_segment = "Text not valid"
        bot.delete_message(message.chat.id, message.message_id)
        result_text = "Received message with adult content from user: " + message.from_user.first_name + \
            "(@" + message.from_user.username + \
            "): [" + invalid_text_segment + \
                      "]. We notified admin's of the current chat."
        notify_admins(message.chat.id, result_text)

    if (not check_text_result) and message_photo:
        img_data = bot.get_file(message_photo[-1].file_id).wait()
        img_url = BASE_IMAGE_URL.format(API_KEY, img_data.file_path)
        check_image_result = check_image(img_url)

    if (not check_text_result) and message_sticker:
        img_data = bot.get_file(message_sticker.file_id).wait()
        img_url = BASE_IMAGE_URL.format(API_KEY, img_data.file_path)
        check_image_result = check_image(img_url)

    if check_image_result:
        bot.delete_message(message.chat.id, message.message_id)
        invalid_text_segment = "Media not valid"
        result_text = "Received message with adult content from user: " + message.from_user.first_name + \
            "(@" + message.from_user.username + \
            "): [" + invalid_text_segment + \
                      "]. We notified admin's of the current chat."
        notify_admins(message.chat.id, result_text)

# @bot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
# def default_command(message):
#     bot.send_message(message.chat.id, "This is the default command handler.")


bot.infinity_polling()
