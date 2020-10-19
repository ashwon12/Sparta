import requests
from bs4 import BeautifulSoup

# requests 라이브러리 설정
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

# bs4 라이브러리 설정
soup = BeautifulSoup(data.text, 'html.parser')
tr_list = soup.select("#old_content > table > tbody > tr")

for tr in tr_list:
    a_tag = tr.select_one("td.title > div > a")
    if a_tag is not None:
        title = a_tag.text
        rank = tr.select_one("td:nth-child(1) > img")['alt']
        num = tr.select_one('.point').text
        print(rank,title,num)