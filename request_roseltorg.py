import requests
from bs4 import BeautifulSoup
from aiogram.utils.markdown import link
from datetime import datetime


HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'}


def site_request(date_now, title): # СДЕЛАТЬ ПОИСК НА СЛЕД. СТРАНИЦЕ!!!(параментр page: 1)
    data = {'sale': 0,
        'query_field': title,
        'status[]': 5,
        'status[]': 0,
        'currency': 'all',
        'start_date_published': '05.04.23'}
    responce = requests.get('https://www.roseltorg.ru/procedures/search_ajax', headers=HEADERS, params=data)
    soup = BeautifulSoup(responce.text, 'lxml').find_all('div', {'class': "search-results__item"})
    list_of_answers = []
    for obj in soup:
        number = obj.find('div', {'class': 'search-results__lot'}).text.rstrip().lstrip()
        name = obj.find('div', {'class': 'search-results__subject'}).text.rstrip().lstrip()
        customer = obj.find('div', {'class': 'search-results__customer'}).text.rstrip().lstrip()
        price = obj.find('div', {'class': 'search-results__sum'}).find('p', {}).text.rstrip().lstrip() + ' руб.'
        date = obj.find('time', {'class': 'search-results__time'})
        end_date = date.find('span', {}).text.rstrip().lstrip()[1:-1] + f' ({date.text[:11].rstrip().lstrip()})'
        more_info = 'https://www.roseltorg.ru/' + obj.find('a', {'class': 'search-results__link'})['href']
        text = f'Номер: {number}\n\
Наименование: {name}\n\
Заказчик: {customer}\n\
Цена: {price}\n\
Осталось времени на подачу: {end_date}\n\
{more_info}\n'
        list_of_answers.append(text)
    return list_of_answers