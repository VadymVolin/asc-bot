import telebot
import PIL
from PIL import Image
from requests import get

#Сюда подставляете свой токен
bot = telebot.TeleBot('2059855205:AAEX2RnnkBQWnLHxw3PMx5JcYaZhGGvE_9E')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Пришли мне Emoji, который необходимо сделать размытым.')
                     
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'нам первый смайлик':
        img = open('Смайлики и люди 1.png', 'rb')
        
        bot.send_document(message.chat.id, img) 
    elif message.text.lower() == 'наш второй смайлик':
        img = open('Смайлики и люди 2.png', 'rb')
        bot.send_document(message.chat.id, img)    
   
    else:
        bot.send_message(message.chat.id, 'Прости, но пока у меня нет этих Emoji')

bot.polling()
#сами смайлики прописать не могу, иначе публикация не обрабатывается на habr