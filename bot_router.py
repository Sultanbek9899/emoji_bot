from aiogram import Bot, Dispatcher


from bot_utils.handlers import welcome_message
from config import TOKEN


bot = Bot(token=TOKEN)


dp = Dispatcher(bot)

dp.register_message_handler(welcome_message, commands=["start"])
