#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-11-9

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


from functools import reduce
#===============================================================================
# 
#===============================================================================
def square(x) :         # 计算平方数
    return x ** 2

def add(x, y) :            # 两数相加
    return x + y

def is_odd(n):
    return n % 2 == 1

def map_test():
    a = map(square, [1,2,3,4,5])
    print(type(a))
    b = list(a)
    print(b)
    c = map(lambda x,y:x+y,[1,4,5],[2,3,5,7])
    print(list(c))

def reduce_test():
    sum1 = reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
    sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
    print(sum1)
    print(sum2)

def filter_test():
    newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(list(newlist))
    newlist2 = filter(lambda x:x%2==0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(list(newlist2))

if __name__ == '__main__':
    map_test()
    reduce_test()
    filter_test()