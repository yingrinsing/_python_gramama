#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2017-9-25

@author: yingrinsing
"""

if __name__ == '__main__':
    a = 1
    b = 0.05
    a += 1

    # 三目表达式
    print(a if a > b else b)

    # 常规if表达式
    if a > b:
        print(a)
    else:
        print(b)

    # 多级if表达式，python不支持switch表达式
    if a < 1:
        print(1)
    elif a < 3:
        print(2)
    else:
        print(3)
