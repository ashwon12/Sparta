import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# requests 라이브러리 설정
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)

# bs4 라이브러리 설정
soup = BeautifulSoup(data.text, 'html.parser')
tr_list = soup.select("#body-content > div.newest-list > div > table > tbody > tr")

# mongoDB 설정
client = MongoClient('localhost', 27017)
db = client.genieMusic

for tr in tr_list:
    rank = tr.select_one("td.number").text[0:2].strip()
    title = tr.select_one("td.info > a.title.ellipsis").text.strip()
    singer = tr.select_one("td.info > a.artist.ellipsis").text.strip()
    print(rank, title, singer)

    doc = {
        'rank': rank,
        'title': title,
        'singer': singer
    }
    db.genieMusic.insert_one(doc)
