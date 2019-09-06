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
    for i in xrange(3):  
        for j in xrange(6):
            print i, j
            if j == 3:
                break  
        else:  
            continue  
        break


if __name__ == '__main__':
    basic_for()