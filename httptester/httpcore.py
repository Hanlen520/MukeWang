# -*- coding:utf-8 -*-
'''
时间：2018-6-12
作者：浪晋
说明：实现对requests的二次封装
'''
import requests

def http_request(request):
    method = request.pop("method")
    url = request.pop("url")
    kwargs = request
    response = requests.request(method, url, **kwargs)
    print(response.json())
    return response