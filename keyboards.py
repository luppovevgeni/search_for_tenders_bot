from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import available_sites


posting_time = InlineKeyboardButton('Настройки рассылки', callback_data='posting')
keywords = InlineKeyboardButton('Ключевые слова', callback_data='keywords')
site = InlineKeyboardButton('Доступные сайты', callback_data='site')
filters = InlineKeyboardButton('Фильтры для поиска', callback_data='in_developing')
personal_area = InlineKeyboardMarkup(row_width=1)
personal_area.add(posting_time, keywords, site, filters)


back_home = InlineKeyboardButton('Назад', callback_data='home')
change_keywords = InlineKeyboardButton('Изменить', callback_data='change_keywords')
keywords_settings = InlineKeyboardMarkup(row_width=2)
keywords_settings.add(change_keywords, back_home)


home = InlineKeyboardMarkup(row_width=2)
home.add(back_home)


change_time = InlineKeyboardButton('Изменить время', callback_data='change_time')
del_time = InlineKeyboardButton('Отазаться от рассылки', callback_data='del_time')
week_days = InlineKeyboardButton('Дни недели', callback_data='week_days')
time_settings = InlineKeyboardMarkup(row_width=1)
time_settings.add(change_time, week_days, del_time, back_home)

week = ['Понедельник',
        'Вторник',
        'Среда',
        'Четверг',
        'Пятница',
        'Суббота',
        'Воскресенье']

def day(days):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for i in range(7):
        if str(i) in days:
            button = InlineKeyboardButton(week[i] + '✅', callback_data=f'day_{i}')
        else:
            button = InlineKeyboardButton(week[i] + '❌', callback_data=f'day_{i}')
        keyboard.insert(button)
    back_posting = InlineKeyboardButton('Назад', callback_data='posting')
    keyboard.insert(back_posting)
    return keyboard


def site(sites):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for site in available_sites:
        if site in sites:
            button = InlineKeyboardButton(site + '✅', callback_data=f'site_{site}')
        else:
            button = InlineKeyboardButton(site, callback_data=f'site_{site}')
        keyboard.insert(button)
    keyboard.insert(back_home)
    return keyboard
