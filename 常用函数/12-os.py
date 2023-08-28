#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018-2-11

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
import os
#===============================================================================
# 
#===============================================================================
def _lktest():
    obj = None
    laok.dump_description_help(obj)
    path1 = r'E:\gitcode\Aqlicai_RFS\APIFullTest\DataSource\TotalRestuls\test.txt'
    print os.path.split(path1)
    print os.path.splitdrive(path1)
    print os.path.splitext(path1)
    print os.path.splitunc(path1)
    #把路径分割成dirname和basename，返回一个元组
    #os.path.splitdrive(path)   #一般用在windows下，返回驱动器名和路径组成的元组
    #os.path.splitext(path)  #分割路径，返回路径名和文件扩展名的元组
    #os.path.splitunc(path)  #把路径分割为加载点与文件


if __name__ == '__main__':
    laok.lktest_run()#catch_except = True