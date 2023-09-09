import requests

url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5%20%D0%BE%D0%B1%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5'
params = {'searchString': 'техническое обследование'}
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
print(response.text)