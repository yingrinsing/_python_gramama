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


def lambda_study20230223():
    func = lambda x, y: x*y
    print(func(2, 3))
    func1 = lambda x: x%3
    list1 = [func1(x) for x in range(10)]
    for i in list1:
        print(i)



if __name__ == '__main__':
    lambda_study20230223()
