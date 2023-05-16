#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-11-8

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
import tushare as ts
#===============================================================================
# 
#===============================================================================
def _lktest():
    obj = ts.trade_cal()
    #laok.dump_description_help(obj)
#     print ts.is_holiday('2017-01-01')
#     print ts.is_holiday('2017-09-22')
    print ts.get_k_data(code = '000002.SZ')

if __name__ == '__main__':
    laok.lktest_run()#catch_except = True