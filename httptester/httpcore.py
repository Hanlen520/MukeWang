# -*- coding:utf-8 -*-
'''
时间：2018-6-12
作者：浪晋
说明：实现对requests的二次封装
'''
import requests
from testcase import chick_request_context
requests.packages.urllib3.disable_warnings()

class HttpCore():
    def __init__(self,request):
        self.request = chick_request_context(request)

    def run(self):
        request = self.request
        method = request.pop("method")
        url = request.pop("url")
        kwargs = request
        response = requests.request(method, url, **kwargs)

        return response