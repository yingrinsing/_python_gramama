#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018-1-4

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""
import shutil
#===============================================================================
 
def test():
    shutil.copy(r'D:\RobotFramework\Robot_Report',r'E:\gitcode\Aqlicai_RFS\APITest\DataSource\TotalRestuls\notice\notice_01')

if __name__ == '__main__':
    #laok.lktest_run()#catch_except = True
    #shutil.rmtree(r'E:/test')
    shutil.rmtree('data/input/auto') 
    #test()