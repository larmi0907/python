import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200325',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# 과제 : 순위 / 곡 제목 / 가수 (네이버영화 실습과 동일하게 진행)

# 1. 지니 홈페이지에서 tr을 변수로 저장, 불러오기
musicChart = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# 페이지에 있는 '순위 / 곡 제목 / 가수' 받아오기
rank = 0
for i in musicChart:
    titName = i.select_one('td.info > a')
    artName = i.select_one('td.info > a.artist.ellipsis')
    if titName is not None:
        rank += 1
        title = titName.text.strip()
        artist = artName.text
        print(rank, title,'-', artist)
