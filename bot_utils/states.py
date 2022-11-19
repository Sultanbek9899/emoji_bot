from aiogram.dispatcher.filters.state import StatesGroup,State




class UserMessageState(StatesGroup):
    answer_text = State()
    