from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://misiani:asi2742871@cluster0.kqin5.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/fanpage", methods=["POST"])
def web_mars_post():
    nick_receive = request.form['nick_give']
    cheer_receive = request.form['cheer_give']
    today_receive = request.form['today_give']
    doc = {
        'nick': nick_receive,
        'cheer': cheer_receive,
        'time' : today_receive
    }
    db.bami_fan_page.insert_one(doc)  # post로받은값들을db에바로저장시키기
    return jsonify({'msg': '데이터 업로드 완료!'})

@app.route("/fanpage", methods=["GET"])
def web_mars_get():
    # GET요청받으면,marsdb에서find모두찾기로리스트에담아변수저장
    order_list = list(db.bami_fan_page.find({}, {'_id': False}))
    # returnjsonify({'msg':'GET연결완료!'})
    return jsonify({'orders': order_list})  # 요청한것을'orders'에실어서order_list의모든주문목록을보내줌
    
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

a = 324
