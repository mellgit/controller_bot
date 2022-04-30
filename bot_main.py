from telebot import *
import re
import logging

from config import *
import command_os
import command_google


logger = logging.getLogger("tg-bot")
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

bot = telebot.TeleBot(key)




@bot.message_handler(commands=['help'])
def help(message):
    hellper = """
    instruction
    b...
    """

    bot.send_message(message.chat.id, hellper)


# метод для команд (основное меню)
@bot.message_handler(commands=['menu'])
def menu(message): 


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    linux_bot = types.KeyboardButton('shutdown')
    markup.add(linux_bot)

    # command_os.voice()

    bot.send_message(message.chat.id, 'Здравствуйте, сэр', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def menu_responce(message):

    
    if re.finditer("загугли ", message.text):
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



    if message.text == "yep":
        
        bot.send_message(message.chat.id, "готово")
    
        # command_os.voice()
        menu(message)
        # command_os.kill_and_shutdown()









bot.polling(none_stop=True)
