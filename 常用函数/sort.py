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


if __name__ == '__main__':
    # d = [
    #     {"name":"张三","age":34},
    #     {"name": "李四", "age": 21}
    # ]
    # print(d)
    # # d.sort(key=lambda x:x["age"])
    # e=sorted(d,key=lambda x:x["age"])
    # print(e)

    l1 = ['b','c','d','b','c','a','a']
    l2 = list(set(l1))
    print(l2)
    for i in l2:
        print(l1.index(i))
    l2.sort(key=l1.index)
    print(l2)