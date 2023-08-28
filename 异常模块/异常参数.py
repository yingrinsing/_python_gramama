#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-9-30

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""



#===============================================================================
# 
#===============================================================================
#__class__
#attribute---->
    #args[<type 'getset_descriptor'>] [<attribute 'args' of 'exceptions.BaseException' objects>]
    #message[<type 'getset_descriptor'>] [<attribute 'message' of 'exceptions.BaseException' objects>]
#funcs/method---->
    #__init__(...) ==>x.__init__(...) initializes x; see help(type(x)) for signature
    
def lktest():
    try:
        float(['a',1])
    except Exception as diag:
        pass
    print('[%s]:[%s]' % (diag,type(diag)))
    shuxing = diag.__class__
    name = diag.__class__.__name__
    doc = diag.__class__.__doc__
    print(shuxing)
    print(name)
    print(doc)
    obj = name
    


if __name__ == '__main__':
    lktest()#catch_except = True