from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.shop  # 'shop' 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('homework.html')


## API 역할을 하는 부분
@app.route('/list', methods=['POST'])
def write_list():
    # 1. 클라이언트가 준 이름name, 수량selectNum, 주소Adress, 휴대폰번호Number 가져오기.
    name_recive = request.form['name_give']
    num_recive = request.form['num_give']
    adress_recive = repuest.form['adress_give']
    number_recive =request.form['number_give']

list = {
  'name' : name_recive,
  'select' : select_recive,
  'adress' : adress_recive,
  'number' : number_recive
}

    # 2. DB에 정보 삽입하기
   db.manylist.insert_one(list)
    # 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result':'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})


@app.route('/list', methods=['GET'])
def read_list():
    return jsonify({'result':'success', 'msg': '리뷰를 성공적으로 받아왔습니다'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)