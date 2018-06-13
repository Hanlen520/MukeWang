# -*- coding:utf-8 -*-
'''
时间：2018-6-12
作者：浪晋
说明：实现对测试用例的读取
'''
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
def import_json_file(testcass):
    with open(testcass,"r") as f:
        testcass = json.load(f)
        print(testcass)
    return testcass