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
def import_json_file(json_file_name):
    with open(json_file_name,"r") as f:
        testcass = json.load(f)
    request = testcass.get("request")
    validata = testcass.get("validata")
    if request not is None and validata not is None:
        print(testcass)
        return request, validata
    else:
        print("用例中不存在我们需要的参数")
        exit()

def chick_json_type(json_file_name):
    '''
    test_cass.json
    '''
    json_type = json_file_name.split(".")
    # print(json_type)
    if json_type[1] == "json" and json_file_name.startswith("test"):
        return json_file_name
    else:
        print("导入的用例格式不正确！")
        exit()


def chick_request_context(request):
    '''
    {
        "method":"POST",
        "url":"http://127.0.0.1:8808/login",
        "json":{"username":"admin","password":"123456"},
        "headers":{"Content-Type": "application/json"}
    }
    '''
    methodlist = ["GET","POST","DELETE"]
    if "method" not in request:
        print("method不存在request参数中,默认使用GET")
        request["method"] = "GET"
    if request["method"] not in methodlist:
        print("method不存在request参数中,默认使用GET")
        request["method"] = "GET"
    if "url" not in request:
        print("url不存在request参数中,请检查参数")
        raise
    return request
    
def chick_validata_context(validata):
    '''
    "validata":[200,200]
    '''
    if len(validata["validata"]) == 2:
        return validata
    else:
        print("validata不正确,请检查参数")
        raise