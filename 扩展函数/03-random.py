#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-11-1

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
import random
import uniout
import itertools
import time
#===============================================================================
# 
#===============================================================================
def lktest():
    obj = None
    
    list = ['你好','不','长荣股份','鹏翎股份','天舟文化','天马股份','天齐锂业']
    print len(list)
    #laok.dump_description_help(combinations(list, 2))
#     iter1= itertools.combinations(list, 2)
#     print list(iter1)
#     for name in itertools.combinations(list, 2):
#         print name
#     print list(itertools.combinations([1,2,3,4],2))
    #list1 = itertools.combinations(list, 2)
    #print list(list1)
    #slice = random.sample(itertools.combinations(list, 2), 5)
    #print list
    #print slice
#求n的阶层
def factorial(n):
    return reduce(lambda x,y:x*y,[1]+range(1,n+1))

def factorial_1(n,m):
    if n>m:
        return reduce(lambda x,y:x*y,[1]+range(n,n-m,-1))
    else:
        return 1

"""
#MAX>=7,当m最大为5时
m为组合C(n,m)中的m值，求不超过MAX的最大n
MAX为组合指标最大所取的量
"""
def count_random_num(m,MAX):
    f = MAX *factorial(m)
    p = int(power(f,1.0/m))
    end = p+m
    n = p-1 if p>1 else 1
    if n<1:
        n=1
    for i in xrange(n,end):
        #print i, factorial_1(i,m)
        if factorial_1(i,m)<=f:
            n =i
        else:
            break
    return n

def count_random_num1(m,n_max,MAX):
    f = MAX *factorial(m)
    p = int(power(f,1.0/m))
    end = p+m
    n = p-1 if p>1 else 1
    try:    
        for i in xrange(n,end):
            #print i, factorial_1(i,m)
            if factorial_1(i,m)>=f:
                n = i if i<=n_max else n_max
    except:
        n=1
    if n<1:
        n=1
    return n

if __name__ == '__main__':
    lktest()#catch_except = True
    timestring = '2016-12-21 10:22:56'
    print time.mktime(time.strptime(timestring, '%Y-%m-%d %H:%M:%S'))