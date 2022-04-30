
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


markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
# website = types.KeyboardButton('google')
# linux_bot = types.KeyboardButton('shutdown')
# markup.add(linux_bot)



@bot.message_handler(commands=['help'])
def help(message):
    hellper = """
    instruction
    buttons:
        google - открывает гугл
        shutdown - выкл пк
    """

    bot.send_message(message.chat.id, hellper, reply_markup=markup)


# метод для команд (основное меню)
@bot.message_handler(commands=['start'])
def menu(message): 
    linux_bot = types.KeyboardButton('shutdown')


    markup.add(linux_bot)
    command_os.voice()

    bot.send_message(message.chat.id, 'Здравствуйте, сэр', reply_markup=markup)


# метод для обработки текста, после кнопок
@bot.message_handler()
def menu_responce(message):

    # открывает гугл
    # if message.text 
    # google_searsh = re.finditer("загугли ", message.text)
    if re.finditer("загугли ", message.text):
        search = ' '.join(message.text.split()[1:])
        url = f"https://www.google.com/search?q={search}"  # ссылка для поиска чего либо
        webbrowser.open(url, new=0, autoraise=True)
        # command_os.voice()

        bot.send_message(message.chat.id, f'гуглю: {search}')

    # поиск по указанной ссылке
    # open_link = re.search("https?://[\w.-]+", message.text)

    if re.search("https?://[\w.-]+", message.text):
        url = message.text  # ссылка для поиска чего либо
        webbrowser.open(url, new=0, autoraise=True)
        bot.send_message(message.chat.id, f'open: {message.text}')

    if message.text == "shutdown":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        yep = types.KeyboardButton('yep')
        markup.add(yep)
        bot.send_message(message.chat.id, 'вы уверены?', reply_markup=markup)

    if message.text == "yep":
        
        bot.send_message(message.chat.id, reply_markup=markup)
        # menu(message)
        # command_os.kill_and_shutdown()









bot.polling(none_stop=True)
