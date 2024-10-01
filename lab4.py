import telebot
from telebot.types import Update

token = "8094492932:AAF4W8ucV74rUM2ht9G5cWdoMmBHF8dAKtY"


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
	bot.reply_to(message, message.text)





bot.polling(none_stop=True)



