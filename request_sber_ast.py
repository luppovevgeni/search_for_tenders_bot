import requests, ast
from bs4 import BeautifulSoup
from datetime import datetime
from aiogram.utils.markdown import link


HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'}
def site_request(date_now, title):
    data = {'xmlData': f'<elasticrequest><personid>0</personid><buid>0</buid><filters><mainSearchBar><value>{title}</value><type>phrase_prefix</type><minimum_should_match>100%</minimum_should_match></mainSearchBar><purchAmount><minvalue></minvalue><maxvalue></maxvalue></purchAmount><PublicDate><minvalue></minvalue><maxvalue></maxvalue></PublicDate><PurchaseStageTerm><value></value><visiblepart></visiblepart></PurchaseStageTerm><SourceTerm><value></value><visiblepart></visiblepart></SourceTerm><RegionNameTerm><value></value><visiblepart></visiblepart></RegionNameTerm><RequestStartDate><minvalue></minvalue><maxvalue></maxvalue></RequestStartDate><RequestDate><minvalue></minvalue><maxvalue></maxvalue></RequestDate><AuctionBeginDate><minvalue></minvalue><maxvalue></maxvalue></AuctionBeginDate><okdp2MultiMatch><value></value></okdp2MultiMatch><okdp2tree><value></value><productField></productField><branchField></branchField></okdp2tree><classifier><visiblepart></visiblepart></classifier><orgCondition><value></value></orgCondition><orgDictionary><value></value></orgDictionary><organizator><visiblepart></visiblepart></organizator><CustomerCondition><value></value></CustomerCondition><CustomerDictionary><value></value></CustomerDictionary><customer><visiblepart></visiblepart></customer><PurchaseWayTerm><value></value><visiblepart></visiblepart></PurchaseWayTerm><PurchaseTypeNameTerm><value></value><visiblepart></visiblepart></PurchaseTypeNameTerm><BranchNameTerm><value></value><visiblepart></visiblepart></BranchNameTerm><isSharedTerm><value></value><visiblepart></visiblepart></isSharedTerm><notificationFeatures><value></value><visiblepart></visiblepart></notificationFeatures><statistic><totalProc>24</totalProc><TotalSum>50.43 Млн.</TotalSum><DistinctOrgs>16</DistinctOrgs></statistic></filters><fields><field>TradeSectionId</field><field>purchAmount</field><field>purchCurrency</field><field>purchCodeTerm</field><field>PurchaseTypeName</field><field>purchStateName</field><field>BidStatusName</field><field>OrgName</field><field>SourceTerm</field><field>PublicDate</field><field>RequestDate</field><field>RequestStartDate</field><field>RequestAcceptDate</field><field>EndDate</field><field>CreateRequestHrefTerm</field><field>CreateRequestAlowed</field><field>purchName</field><field>BidName</field><field>SourceHrefTerm</field><field>objectHrefTerm</field><field>needPayment</field><field>IsSMP</field><field>isIncrease</field><field>purchType</field></fields><sort><value>default</value><direction></direction></sort><aggregations><empty><filterType>filter_aggregation</filterType><field></field></empty></aggregations><size>20</size><from>0</from></elasticrequest>',
             'orgId': 0,
             'targetPageCode': 'UnitedPurchaseList',
             'PID': 0}
    responce = requests.post('https://www.sberbank-ast.ru/SearchQuery.aspx?name=Main', headers=HEADERS, data=data)
    a = ast.literal_eval(ast.literal_eval(responce.text)['data'])['tableXml']
    xml = BeautifulSoup(a, 'xml').find_all('hits', {})
    list_of_answers = []
    for soup in xml:
        data = soup.find('_source', {})
        date = data.find("PublicDate", []).text
        day1, m1, y1 = list(map(lambda x: int(x), date.split(' ')[0].split('.')))
        h1, minute1 = list(map(lambda x: int(x), date.split(' ')[1].split(':')))
        public_date = datetime(y1, m1, day1, h1, minute1)
        d1 = public_date - date_now
        if d1.days == -1:
            date = data.find("RequestDate", []).text
            day, m, y = list(map(lambda x: int(x), date.split(' ')[0].split('.')))
            h, minute = list(map(lambda x: int(x), date.split(' ')[1].split(':')))
            request_date = datetime(y, m, day, h, minute)
            d = request_date - date_now
            text = f'Номер: {data.find("purchCodeTerm", []).text.rstrip()}\n\
Наименование: {data.find("purchName", []).text.rstrip()}\n\
Заказчик: {data.find("OrgName", []).text.rstrip()}\n\
Цена: {data.find("purchAmount", []).text.rstrip() + " руб." if data.find("purchAmount", []) != None else "НЕТ"}\n\
Осталось времени на подачу: {d.days} дней ({date})\n\
{data.find("objectHrefTerm", []).text}\n'
            list_of_answers.append(text)
    return list_of_answers


#print(site_request(datetime.now(), 'Техническое обследование'))