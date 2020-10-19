import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)

# bs4 라이브러리 설정
soup = BeautifulSoup(data.text, 'html.parser')
baseball_list = soup.select('#regularTeamRecordList_table > tr')

for tr in baseball_list:
    team_name = tr.select_one('.tm span').text
    team_rank = tr.select_one('th').text
    team_win = tr.select_one('td > strong').text

    if float(team_win) > 0.5:
        print(team_rank, team_name, team_win)
