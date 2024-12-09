from functools import wraps
import telebot

# Декоратор для логування викликів функцій
def log_command(func):
    @wraps(func)
    def wrapper(message, *args, **kwargs):
        command = message.text
        user = message.from_user.username or "анонім"
        print(f"Команда '{command}' викликана користувачем @{user}")
        return func(message, *args, **kwargs)
    return wrapper
