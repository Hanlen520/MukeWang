# -*- coding:utf-8 -*-
'''
时间：2018-6-12
作者：浪晋
说明：实现对预期结果和实际结果的判断
'''

def chick_response(response, validata):
    code = eval(validata[0])
    assert code == validata[1]
    print("测试通过")