# -*- coding:utf-8 -*-
'''
时间：2018-6-12
作者：浪晋
说明：实现对预期结果和实际结果的判断
'''

def get_assert(validatas):
    assertdict ={
        "Equal": equal_validata,
        "NotEqual": notequal_validata,
        "Is": "is",
        "IsNot": "is not",
        "In": "in",
        "NotIn": "not in"
    }
    fuclist = []
    for value in validatas:
        
        key = list(value.keys())[0]
        print("key:" ,key)
        assrctfuc = assertdict[key]
        fuclist.append(assrctfuc)
    return fuclist

def equal_validata(validata):
    '''
    "validata":[{"Equal":200,200]},{}]
    '''
    first = validata[0]
    second = validata[1]
    print(first,"==",second)
    assert first == second

def notequal_validata(validata):
    '''
    "validata":[{"Equal":200,200]},{}]
    '''
    first = validata[0]
    second = validata[1]
    print(first,"!=",second)
    assert first != second

def chick_response(validatas):
    valilist = []
    for value in validatas:
        key = list(value.keys())[0]
        print("key:" ,key)
        valilist.append(value[key])
    fuclist = get_assert(validatas)
    num = 0
    for fuc in fuclist:
        fuc(valilist[num])
        num += 1