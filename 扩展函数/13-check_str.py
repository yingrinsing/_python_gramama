#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018-3-20

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
import re
#===============================================================================
# 
#===============================================================================
def judge_pure_english(keyword):  
    return all(ord(c) < 128 for c in keyword)  
 
def judgy2(keyword):   
    t = re.match('^[0-9a-zA-Z|\s]+$',keyword)
    print t
    if re.match('^[0-9a-zA-Z|\s]+$',keyword):
        print('符合要求')
    else:
        print('不符合要求')

if __name__ == '__main__':
#     print judge_pure_english("你好r")
#     print judge_pure_english("你好")
#     print judge_pure_english("rA")
    judgy2("你好r")
    judgy2("你好")
    judgy2("KGI I")