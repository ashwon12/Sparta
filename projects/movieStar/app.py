from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분 , read
@app.route('/api/list', methods=['GET'])
def show_stars():
    movie_list = list(db.mystar.find({}, {'_id': False}).sort('like',-1))

    return jsonify({'result': 'success','movieList':movie_list})


# 좋아요 눌렀을 경우 update
@app.route('/api/like', methods=['POST'])
def like_star():
    name_receive = request.form['name_give']

    db.mystar.update_one({'name': name_receive}, {'$inc': {'like': 1}})

    # movie_star = db.mystar.find_one({'name': name_receive})
    # new_like = movie_star['like']+1
    # db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})

    return jsonify({'result': 'success', 'msg': name_receive +"의 좋아요가 눌려졌어요!👍"})


# 삭제 눌렀을 경우 Delete
@app.route('/api/delete', methods=['POST'])
def delete_star():
    name_receive = request.form['name_give']

    db.mystar.delete_one({'name': name_receive})

    return jsonify({'result': 'success', 'msg': name_receive +"의 정보가 삭제됩니다 😥"})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
