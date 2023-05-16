#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-11-1

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
from numpy import power
#===============================================================================
# 
#===============================================================================
def _lktest():
    obj = None
    laok.dump_description_help(obj)
    list = [  0,   1,   8,  27,  64, 125]
    
    a = power(list,1.0/3)
    print a
    b = power(10000000/19,1.0/3)
    print b,int(b)
    
def get_value(n):  
    if n==1:  
        return n  
    else:  
        return n * get_value(n-1)  
          
def gen_last_value(n,m):  
     first = get_value(n)  
     print "n:%s     value:%s"%(n, first)  
     second = get_value(m)  
     print "n:%s     value:%s"%(m, second)  
     third = get_value((n-m))  
     print "n:%s     value:%s"%((n-m), third)  
     return first/(second * third)  
 
import copy    #实现list的深复制
  
def combine(lst, l):
    result = []
    tmp = [0]*l
    length = len(lst)
    def next_num(li=0, ni=0):
        if ni == l:
            result.append(copy.copy(tmp))
            return
        for lj in range(li,length):
            tmp[ni] = lst[lj]
            next_num(lj+1, ni+1)
    next_num()
    return result          
          
if __name__ == "__main__":  
    # C(12,5)  
    #rest = gen_last_value(3000,1)  
    #print "value:", rest 
    print combine(3000,2)