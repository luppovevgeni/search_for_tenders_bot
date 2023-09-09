import requests, json
from bs4 import BeautifulSoup
from datetime import datetime
from aiogram.utils.markdown import link


HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'}


def site_request(date_now, title):
    data ={'name': title,
            'page': 1,
            'sort': "datePublished_desc"}
    responce = requests.post('https://www.tektorg.ru/api/getProcedures', headers=HEADERS, data=data)
    data = json.loads(responce.text)['data']
    list_of_answers = []
    for obj in data:
        number = obj['registryNumber']
        name = obj['title']
        print(name)
        customer = obj['organizerName']
        price = f'{obj["sumPrice"]} руб.' if obj['sumPrice'] != 'НМЦ не установлена' else 'НЕТ'
        date = obj['dates']['datePublished'].split('+')[0]
        y, m, day = list(map(lambda x: int(x), date.split('T')[0].split('-')))
        h, minute, s = list(map(lambda x: int(x), date.split('T')[1].split(':')))
        p_date = datetime(y, m, day, h, minute)
        print(p_date)
        if (date_now - p_date).days == 1:
            date = obj['dates']['dateEndRegistration'].split('+')[0]
            y, m, day = list(map(lambda x: int(x), date.split('T')[0].split('-')))
            h, minute, s = list(map(lambda x: int(x), date.split('T')[1].split(':')))
            e_date = datetime(y, m, day, h, minute)
            end_date = f'{(e_date - date_now).days} дней ({day}.{m}.{y} в {h}:{minute})'
            more_info = f'https://www.tektorg.ru/{obj["sectionAlias"]}/procedures/{obj["id"]}'
            text = f'Номер: {number}\n\
Наименование: {name}\n\
Заказчик: {customer}\n\
Цена: {price}\n\
Осталось времени на подачу: {end_date}\n\
{more_info}\n'
            list_of_answers.append(text)
    return list_of_answers


'''a = site_request(datetime.now(), 'техническое обследование')
for elem in a:
    print(elem)'''