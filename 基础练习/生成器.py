#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""

# ===============================================================================
# 
# ===============================================================================
class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> 无穷数列

    def __iter__(self):
        # // 把self.begin赋值给result，不过会先强制转换成前面的假发算式得到的类型
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            print(result)
            index += 1
            result = self.begin + self.step * index


if __name__ == '__main__':
    # atr = ArithmeticProgression(1, 3, None)
    # for i in list(atr):
    #     print(i)
    # # print(list(atr))

    # 列表生成器
    a = [i for i in range(0, 10)]
    print(type(a))
    # 生成器表达式
    b = (i for i in range(0, 10))
    print(type(b))

