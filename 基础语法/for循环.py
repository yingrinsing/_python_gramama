#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-11-6

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


#===============================================================================
# 
#===============================================================================


def basic_for():
    for i in range(3):
        for j in range(6):
            print(i, j)
        else:
            print("执行else")
            break


if __name__ == '__main__':
    basic_for()