#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-11-9

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
#===============================================================================
# 
#===============================================================================
def _lktest():
    
    list = []
    print list
    
    for x in xrange(1,6):
        for y in xrange(0,5):
            for z in xrange(0,5):
                if y ==0 and z == 0:
                    list.append([x,y,z])
                elif x*(y+z) <=4:
                    list.append([x,y,z])
    print list,len(list)
                    

if __name__ == '__main__':
    laok.lktest_run()#catch_except = True