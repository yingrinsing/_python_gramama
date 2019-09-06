#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-9-29

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


#===============================================================================
# 
#===============================================================================


if __name__ == '__main__':
    try:
        file1 = open('test', 'r')
    except IOError, e:
        print("could not open file:", e)