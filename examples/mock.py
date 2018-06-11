# -*- conding:utf-8 -*-
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/login",methods=["POST"])
def login():
    '''
    {"username":"admin","password":"123456"}
    '''
    testdata = request.get_json()
    username = testdata.get("username")
    password = testdata.get("password")
    if username == "admin" and password == "123456":
        respone = {}
        respone["code"] = 200
        respone["msg"] = "登陆成功！"
    else:
        respone = {}
        respone["code"] = 400
        respone["msg"] = "登陆失败！"
    return jsonify(respone)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8808)