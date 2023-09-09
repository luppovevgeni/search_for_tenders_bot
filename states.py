from aiogram.dispatcher.filters.state import StatesGroup, State


class posting_time(StatesGroup):
    time = State()

class keywords(StatesGroup):
    keywords = State()