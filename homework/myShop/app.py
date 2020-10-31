from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# DB 연결
client = MongoClient('localhost', 27017)
db = client.myShop


@app.route('/')
def homework():
    return render_template('shop.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    address_receive = request.form["address_give"]
    tell_receive = request.form["tell_give"]
    count_receive = request.form["count_give"]
    color_receive = request.form["color_give"]

    # 3. mongoDB에 데이터 넣기
    doc = {
        'name': name_receive,
        'count': count_receive,
        'color': color_receive,
        'address': address_receive,
        'tell': tell_receive
    }
    db.Orderer_Information.insert_one(doc)

    return jsonify({'result': 'success', 'msg': "주문이 완료되었습니다!"})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    infoList = list(db.Orderer_Information.find({}, {'_id': False}))

    return jsonify({'result': 'success', 'Info': infoList})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
