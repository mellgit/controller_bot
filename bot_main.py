
from telebot import *
import webbrowser
import re
import logging
from time import time, sleep


from config import *
import command_os


logger = logging.getLogger("tg-bot")
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


bot = telebot.TeleBot(key)

"""
смысл таков
1 - отправляешь по кнопка команды
2 - бот обрабатывает текст
3 - выполняет команду из других модулей
"""


# метод для основных кнопок (основное меню)
@bot.message_handler(commands=['start'])
def start(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    website = types.KeyboardButton('site')
    linux_bot = types.KeyboardButton('shutdown')
    markup.add(website, linux_bot)
    
    bot.send_message(message.chat.id, 'Да, сэр', reply_markup=markup)


# метод для обработки текста, после кнопок
@bot.message_handler()
def start_keyboard(message):

    # открывает гугл
    if message.text == "site":

        url = "https://www.google.linux.voice()com/search?q="  # ссылка для поиска чего либо
        # webbrowser.open(url, new=0, autoraise=True)
        command_os.voice()

        bot.send_message(message.chat.id, 'open google')

    # поиск по указанной ссылке
    link = re.search("https?://[\w.-]+", message.text)

    if link:
        url = message.text  # ссылка для поиска чего либо
        webbrowser.open(url, new=0, autoraise=True)
        bot.send_message(message.chat.id, f'open: {message.text}')

    if message.text == "shutdown":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        yep = types.KeyboardButton('yep')
        markup.add(yep)
        bot.send_message(message.chat.id, 'вы уверены?', reply_markup=markup)

    if message.text == "yep":

        start(message)
        command_os.kill_and_shutdown()


# @bot.message_handler(commands=['voice'])
# def start(message):

#     linux.voice()
#     bot.send_message(message.chat.id, 'Да, сэр')


bot.polling(none_stop=True)
