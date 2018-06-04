from flask import Flask, request, jsonify
app  = Flask(__name__)

@app.route("/login",methods=["POST"])
def login():
    '''
    {"userneme":"admin","password":"123456"}
    '''
    data = request.get_json()
    userneme = data["userneme"]
    password = data["password"]
    if userneme == "admin" and password == "123456":
        res = {}
        res["code"] = 200
        res["msg"] = "登陆成功"
    else:
        res = {}
        res["code"] = 400
        res["msg"] = "登陆失败"
    return jsonify(res)



if __name__ == '__main__':
    app.run(debug=True)