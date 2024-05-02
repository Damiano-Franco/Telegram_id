import os
from functools import wraps
import telebot
from telebot import types #add-ons connected
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


LIST_OF_ADMINS = [215981250,6939720968,69200219]
#my_user_id = 215981250


def check_sender(message):
    if message.from_user.id not in LIST_OF_ADMINS:
        bot.reply_to(message, "questo è un bot privato")
        bot.delete_message(message.chat.id, message.message_id)
        return False
    else:
        return True


@bot.message_handler(commands=['aiuto'])
def send_welcome(message):
    if check_sender(message):
        bot.reply_to(message, " i comandi disponibili sono:\n\n"
                              "/id  per sapere l'ID di un contatto dopo averlo condiviso con il bot\n\n"
                              "/messaggi_gruppo  per scaricare i messaggi di un gruppo")

@bot.message_handler(commands=['id'])
def phone(message):

    bot.reply_to(message, 'condividi il contatto di cui vuoi conosere l\'ID')

@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        bot.reply_to(message, "L'ID è: "+str(message.contact.user_id))
        print(message.contact)

@bot.message_handler(commands=['messaggi_gruppo'])
def group_message(message):

    bot.reply_to(message, 'inserisci il nome del gruppo per scaricare i messaggi (in fase di implementazione)')

bot.infinity_polling()