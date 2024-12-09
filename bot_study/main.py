import os
from dotenv import load_dotenv
import telebot
from utils import authors
from handlers import log_command

# Завантаження змінних середовища
load_dotenv()
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN не знайдено в .env файлі")

# Ініціалізація бота
bot = telebot.TeleBot(TOKEN)

# Обробник команди /start
@bot.message_handler(commands=['start'])
@log_command
def send_welcome(message):
    author_list = "\n".join([f"/{key} - {data[0]}" for key, data in authors.items()])
    response = (
        "Привіт! Я бот, який допоможе тобі знайти книги українських авторів.\n\n"
        "Ось список доступних авторів:\n"
        f"{author_list}\n\n"
        "Наприклад, введи команду /shevchenko, щоб побачити книги Тараса Шевченка."
    )
    bot.reply_to(message, response)

# Обробник команд авторів
@bot.message_handler(commands=list(authors.keys()))
@log_command
def show_books(message):
    command = message.text.lstrip("/")
    if command in authors:
        author_name, books = authors[command]
        books_list = "\n".join([f"{title} - [Читати]({link})" for title, link in books])
        bot.reply_to(message, f"Книги {author_name}:\n{books_list}", parse_mode="Markdown")
    else:
        bot.reply_to(message, "Я не знаю такого автора. Використай /start, щоб побачити список доступних авторів.")

# Запуск бота
if __name__ == "__main__":
    print("Бот працює. Натисніть Ctrl+C для зупинки.")
    bot.infinity_polling()
