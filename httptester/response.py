# -*- coding:utf-8 -*-
'''
时间：2018-6-12
作者：浪晋
说明：实现对response的二次封装
'''
from testcase import chick_validata_context

class Response():
    '''
    "validata":[{"Equal":[resjson["code"],200]},{}]
    '''
    def __init__(self,response, validata):
        self.validata = chick_validata_context(validata)
        self.response = response

    def get_response_args(self):
        response = self.response
        try:
            resjson = response.json()
        except:
            restext = response.text
        resheaders = response.headers
        valilist = self.validata
        validatas = []
        for vali in valilist:
            value = list(vali.values())[0]
            print(value)
            asserts = list(vali.keys())[0]
            print(asserts)
            first = eval(value[0])
            second = eval(value[1])
            validict = {}
            validict[asserts] = [first, second]
            validatas.append(validict)
        return validatas