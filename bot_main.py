from telebot import *
import re
import logging
from time import sleep

from config import hello, bay, key
import command_os
import command_google


logger = logging.getLogger("tg-bot")
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

bot = telebot.TeleBot(key)


# помощь
@bot.message_handler(commands=['help'])
def help(message):
    hellper = """
    instruction
    b...
    """

    bot.send_message(message.chat.id, hellper)


# приветствие 
@bot.message_handler(commands=['start'])
def menu(message):

    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    command_os.voice(hello)

    bot.send_message(message.chat.id, 'здравствуйте')
    

# метод для команд (основное меню)
@bot.message_handler(commands=['menu'])
def menu(message): 


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    mixer_but = types.KeyboardButton('mute')
    linux_but = types.KeyboardButton('shutdown')
    mixer_but_pluse = types.KeyboardButton('+')
    mixer_but_minus = types.KeyboardButton('-')

    markup.add(mixer_but_minus, mixer_but, mixer_but_pluse, linux_but)

    bot.send_message(message.chat.id, "меню", reply_markup=markup)
    

@bot.message_handler(content_types=['text'])
def menu_responce(message):

    
    if re.finditer("загугли ", message.text.lower()):
        search = ' '.join(message.text.split()[1:])
        if len(search) != 0:
            command_google.search_google(search)

            bot.send_message(message.chat.id, f'гуглю: {search}')

    if re.search("https?://[\w.-]+", message.text):

        command_google.open_link(message)

        bot.send_message(message.chat.id, f'open: {message.text}')


    if message.text == "shutdown":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        yep = types.KeyboardButton('yep')
        markup.add(yep)
        bot.send_message(message.chat.id, 'вы уверены?', reply_markup=markup)

    if message.text == "mute":

        bot.send_message(message.chat.id, command_os.mixer())
    
    if message.text == "+":

        bot.send_message(message.chat.id, command_os.mixer("+"))


    if message.text == "-":

        bot.send_message(message.chat.id, command_os.mixer("-"))

    
    if message.text == "yep":
        
        bot.send_message(message.chat.id, "досвидания")
    
        command_os.voice(bay)
        sleep(3)
        
        # command_os.shutdown()


    # else:
    #     bot.send_message(message.chat.id, "не распознано")






bot.polling(none_stop=True)
