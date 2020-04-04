from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

target_movie = db.movies.find_one({'title':'어벤져스: 엔드게임'})
score = target_movie['star']
#
# movies = list(db.movies.find({'star':target_star}))
#
# for movie in movies:
#     print(movie['title'])

# 25부터 30위까지의 평점을 0으로 합니다
# db.movies.update_many({'star':str(score)},{'$set':{'star':0}})
#원복시키기
db.movies.update_many({'star':'0'},{'$set':{'star':'9.38'}})