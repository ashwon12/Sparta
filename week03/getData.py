from pymongo import MongoClient

# mongoDB 설정
client = MongoClient('localhost', 27017)
db = client.dbsparta

movie1 = list(db.movie.find({'title': '월-E'}))
target_num=movie1[0]['num']
print(movie1[0]['num'])

db.movie.update_many({'num': target_num}, {'$set': {'num': '5'}})