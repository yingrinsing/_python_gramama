#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-9-25

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""

#===============================================================================
# 可变对象：list dict set
# 不可变对象：tuple string int float bool
# 可以通过 id()观察内存地址值来区分
#===============================================================================


def change(b):
    b += [3]
    print("b的值为%s,地址值为%s" %(b, id(b)))


if __name__ == '__main__':
    a = [1, 2]
    change(a)
    print("a的值为%s,地址值为%s" %(a, id(a)))
