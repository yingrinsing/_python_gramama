#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-9-26

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
#===============================================================================
# 
#===============================================================================
#(1,),<type 'tuple'>
#builtin-method---->
    #count [<type 'builtin_function_or_method'>] [T.count(value) -> integer -- return number of occurrences of value]
    #index [<type 'builtin_function_or_method'>] [T.index(value, [start, [stop]]) -> integer -- return first index of value.  Raises ValueError if the value is not present.]

def _lktest():
    x = (1,)
    print(x)
    laok.dump_description_help(x)
    


if __name__ == '__main__':
    laok.lktest_run()#catch_except = True