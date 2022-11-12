from email.message import Message
from aiogram import types



async def welcome_message(message:types.Message):
    text = """
        Привет. это бот для игры в угадай фильм по эмоджи.
        Чтобы начать игру, отправь мне соообщение "Начать игру".
    """
    await message.answer(text)