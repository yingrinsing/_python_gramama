#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-11-23

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
import numpy
#===============================================================================
# 
#===============================================================================
def _lktest():
    obj = None
    laok.dump_description_help(obj)
    
def isnan1():
    if 'ut' == numpy.nan:
            print 'ut'
    print ('ut' == numpy.nan)
if __name__ == '__main__':
    laok.lktest_run()#catch_except = True