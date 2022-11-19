from aiogram import Bot, Dispatcher


from bot_utils import handlers as hs
from config import TOKEN


bot = Bot(token=TOKEN)


dp = Dispatcher(bot)

dp.register_message_handler(hs.welcome_message, commands=["start"])
dp.register_message_handler(hs.start_game, commands=["start_game"])
dp.register_message_handler(hs.finish_game, commands=["finish_game"])


# Callback buttons handlers

dp.register_callback_query_handler(
    hs.start_with_category, 
    lambda c: str(c.data).startswith("category_") 
)