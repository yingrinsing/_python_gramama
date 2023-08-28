#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-11-7

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""



from collections import OrderedDict
#===============================================================================
# 
#===============================================================================
def _lktest():
    obj = OrderedDict()
    obj['2013-04-30 00:00:00']='a'
    obj['2013-03-31 00:00:00']='b'
    print obj
    print obj.keys()
    print obj.keys()[-1]
    dict= sorted(obj.items(), key=lambda d:d[0]) 
    #laok.dump_description_help(obj)
    


if __name__ == '__main__':
    laok.lktest_run()#catch_except = True