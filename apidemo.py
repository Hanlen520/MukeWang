# -*- conding:utf-8 -*-
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>你好</h1>'

@app.route("/login",methods=["POST"])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if username == 'admin' and password == '123456':
        res = {}
        res['code'] = 200
        res['token'] = 'jbskjdfnslknkauhsaknlasnkj'
        res['msg'] = '登陆成功！'
    else:
        res = {}
        res['code'] = 400
        res['msg'] = '登陆失败！'
    return jsonify(res)

@app.route("/getinfo",methods=["GET"])
def getinfo():
    res = {}
    res["code"] = 200
    res['data'] = {"name":"小明","age":22,"sex":"男"}
    return jsonify(res)




if __name__ == '__main__':
    app.run(debug=True)