import requests, json
from bs4 import BeautifulSoup
from datetime import datetime
from aiogram.utils.markdown import link


HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'}

data = {"page":1,
        "itemsPerPage":10,
        "tradeName":"ремонт",
        "tradeState":"",
        "OnlyTradesWithMyApplications":False,
        "filterPriceMin":"",
        "filterPriceMax":"",
        "filterTradeEasuzNumber":"",
        "showOnlyOwnTrades":True,
        "IsImmediate":False,
        "IsExpire":False,
        "UsedClassificatorType":5,
        "classificatorCodes":[],
        "CustomerFullNameOrInn":"",
        "CustomerAddress":"",
        "ParticipantHasApplicationsOnTrade":"",
        "UseCustomerInn":False,
        "UseCustomerName":True,
        "ZmoFzType":0,
        "ZmoFinanceSourceBudget":True,
        "ZmoFinanceSourceOutOfBudget":True,
        "ZmoFinanceSourceMixedBudget":True,
        "ZmoFinanceSourceMunicipalBudget":False,
        "ZmoFinanceSourceRegionalBudget":False,
        "ZmoFinanceSourceFederalBudget":False,
        "TradeSearchType":50}

responce = requests.post('https://zmo-new-webapi.rts-tender.ru/api/Trade/GetTradesForAnonymous', data=data, headers=HEADERS)
for elem in json.loads(responce.text)['invdata']:
    print('----------------------------------')
    print(elem)

