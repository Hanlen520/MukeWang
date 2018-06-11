# -*- coding:utf-8 -*-
import requests
import json
'''
{   
    "request" : {
        "method":"POST",
        "url":"http://127.0.0.1:8808/login",
        "json":{"username":"admin","password":"123456"},
        "headers":{"Content-Type": "application/json"}
    },
    "validata":[200,200]
}
'''
# url = "http://127.0.0.1:8808/login"
# json = {"username":"admin","password":"123456"}
# headers = {
#     'Content-Type': "application/json"
#     }
# response = requests.request("POST", url, json=json, headers=headers)
# validata = response.json()
# print(validata)

def import_json_file(testcass):
    with open(testcass,"r") as f:
        testcass = json.load(f)
        print(testcass)
    return testcass

def http_request(request):
    method = request.pop("method")
    url = request.pop("url")
    kwargs = request
    response = requests.request(method, url, **kwargs)
    print(response.json())
    return response

def chick_response(response, validata):
    code = eval(validata[0])
    assert code == validata[1]
    print("测试通过")

testcass = "test_cass.json"
testcass = import_json_file(testcass)
request = testcass.get("request")
validata = testcass.get("validata")
response = http_request(request)
chick_response(response, validata)