import requests
from bs4 import BeautifulSoup
from datetime import datetime
from aiogram.utils.markdown import link


HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'}


def site_request(date_now, title):
    data = {'searchString': title}
    responce = requests.get('https://zakupki.gov.ru/epz/order/extendedsearch/results.html', headers=HEADERS, params=data)
    soup = BeautifulSoup(responce.text, 'lxml')
    list_of_answers = []
    data = soup.find_all('div', {'class': 'row no-gutters registry-entry__form mr-0'})
    for elem in data:
        date = elem.find('div', {'class': 'data-block mt-auto'}).find_all('div', {'class': 'data-block__value'})
        day2, m2, y2 = list(map(lambda x: int(x), date[1].text.split('.')))
        placement_date = datetime(y2, m2, day2)
        if (date_now - placement_date).days == 1:
            header = elem.find('div', {'class': 'registry-entry__header-mid__number'}).find('a', {'target': '_blank'})
            number = header.text.rstrip().lstrip()
            more_info = f'https://zakupki.gov.ru{header["href"]}'#link("Подробнее", f'https://zakupki.gov.ru{header["href"]}')
            name = elem.find('div', {'class': 'registry-entry__body-value'}).text
            customer = elem.find('div', {'class': 'registry-entry__body-href'}).find('a', {'target': '_blank'}).text.rstrip().lstrip()
            price = elem.find('div', {'class': 'price-block__value'}).text.rstrip().lstrip() if elem.find('div', {'class': 'price-block__value'}) != None else 'НЕТ'
            if len(date) == 3:
                end_date = date[-1].text
                day, m, y = list(map(lambda x: int(x), end_date.split('.')))
                request_date = datetime(y, m, day)
                d = request_date - date_now
                if d.days < 0:
                    break
                end_date = f'{d.days} дней ({end_date})'
            else:
                end_date = 'нет времени окончания подачи заявок'
            text = f'Номер: {number}\n\
Наименование: {name}\n\
Заказчик: {customer}\n\
Цена: {price}\n\
Осталось времени на подачу: {end_date}\n\
{more_info}\n'
            list_of_answers.append(text)
    return list_of_answers

#print(site_request(datetime.now(), 'техническое обследование'))