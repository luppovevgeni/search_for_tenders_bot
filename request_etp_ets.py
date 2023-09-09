import requests
from bs4 import BeautifulSoup
from datetime import datetime
from aiogram.utils.markdown import link


HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'}


def site_request(date_now, title): # СДЕЛАТЬ ПОИСК НА СЛЕД. СТРАНИЦЕ!!!(параментр page: 1)
    data = {'q': title,
            'page': 1}
    responce = requests.get('https://www.etp-ets.ru/44/catalog/procedure', headers=HEADERS, params=data)
    soup = BeautifulSoup(responce.text, 'lxml').find('table', {}).find_all('tr', {})[1:]
    list_of_answers = []
    i = 2
    if soup[0].find('td', {}).text != 'Данных не найдено':
        for obj in soup:
            date = obj.find('td', {'class': f'row-publication_datetime{" sortable" * i}'}).text.split('(')[0]
            day1, m1, y1 = list(map(lambda x: int(x), date.split(' ')[0].split('.')))
            h1, minute1, s1 = list(map(lambda x: int(x), date.split(' ')[1].split(':')))
            public_date = datetime(y1, m1, day1, h1, minute1, s1)
            d1 = public_date - date_now
            if d1.days == -1:
                number = obj.find('td', {'class': 'row-procedure_name'}).text.rstrip().lstrip().split(' ')[-1][1:-1 ]
                name = obj.find('td', {'class': 'row-procedure_name'}).find('a', {}).text.rstrip().lstrip()
                customer = obj.find('td', {'class': 'row-customer_name'}).find('a', {}).text.rstrip().lstrip()
                price = obj.find('td', {'class': f'row-contract_start_price{" sortable" * i}'}).text.rstrip().lstrip()
                date = obj.find('td', {'class': f'row-request_end_give_datetime{" sortable" * i}'}).text
                i += 1
                day, m, y = list(map(lambda x: int(x), date.split(' ')[0].split('.')))
                h, minute, s = list(map(lambda x: int(x), date.split(' ')[1].split('(')[0].split(':')))
                request_date = datetime(y, m, day, h, minute, s)
                d = (request_date - date_now).days
                if d < 0:
                    break
                else:
                    end_date = f'{d} дней ({date.split("(")[0]})'
                    more_info = obj.find('td', {'class': 'row-procedure_name'}).find('a', {})['href']
                    text = f'Номер: {number}\n\
Наименование: {name}\n\
Заказчик: {customer}\n\
Цена: {price}\n\
Осталось времени на подачу: {end_date}\n\
{more_info}\n'
                    list_of_answers.append(text)
            else:
                i += 1
    return list_of_answers