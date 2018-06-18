# -*- coding:utf-8 -*-
'''
时间：2018-6-12
作者：浪晋
说明：实现对预期结果和实际结果的判断
'''
assertdict ={
    "Equal": "==",
    "NotEqual": "!=",
    "Is": "is",
    "IsNot": "is not",
    "In": "in",
    "NotIn": "not in"
}
def get_assert(validatas):
    valilist = []
    for vali in validatas:
        value = list(vali.values())[0]
        # aa = 
        asserts = assertdict[str(list(vali.keys())[0])]
        first = str(value[0])
        second = str(value[1])
        assertstr = first + asserts + second
        valilist.append(assertstr)
    return valilist


def chick_validata(validatas):
    '''
    "validata":[{"Equal":200,200]},{}]
    '''
    valilist = get_assert(validatas)
    for vali in valilist:
        print(vali)
        assert eval(vali)
        print("测试通过")