import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200325',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#############################
# (입맛에 맞게 코딩)
#############################

rows = soup.select("#old_content > table > tbody > tr")
rank = 1

for row in rows:
    movie_name = row.select_one("div.tit5")
    movie_tit = row.select_one("td.point")
    if movie_name != None:
        # print(movie_name.text.strip())
        # print(rank, movie_name.text.strip(), movie_tit.text)
        print(rank, end=". ")
        print(movie_name.text.strip(), end=". ")
        print(movie_tit.text)
        rank += 1

