#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-10-18

@author: laok@ArgusTech
@email:  1306743659@qq.com
@copyright: Apache License, Version 2.0
"""
import os
from codecs import open
from pprint import pprint
#===============================================================================
# 
#===============================================================================
def read_csv(filename):
    u"""读取csv 格式的文件
    filename:输入读文件的路径
    """
    with open(filename=filename , mode='r', encoding='utf8') as f:
        names = f.readline().strip().split(',')
        for line in f:
            values = line.strip().split(',')
            assert len(names) == len(values), line
            valdict = { name:values[i]
                        for i,name in enumerate(names)
                       }
            yield valdict

def write_csv(filename, iter_data):
    u"""写入csv 格式的文件
    filename:输入写文件的路径
    iter_data:输入可迭代的字典
    """
    fmt_line = None
    with open(filename=filename , mode='w', encoding='utf8') as f:
        for data in iter_data:
            if not fmt_line:
                fmt_line = u",".join( u"{%s}"%k for k in data) + u'\n'
                f.write(fmt_line.replace('{','').replace('}',''))
#             print(fmt_line.format(**data))
            f.write(fmt_line.format(**data))

def read_csv_lktest():
    iter_data = read_csv(u"指标表元数据信息.csv")
    for i,data in enumerate(iter_data):
        print(i,u" ".join(u"%s:%s"%item for item in data.iteritems()))
     
def write_csv_lktest():
    iter_data = read_csv(u"指标表元数据信息.csv")
    write_csv(u"指标表元数据信息-write.csv", iter_data)
# 写文件

_cache_file = {}
def write_file(filename, msg):
    if filename not in _cache_file:
        _cache_file[filename] = open(filename, mode='a', encoding='utf-8')
    # print(filename)
    # _cache_file[filename].write(codecs.BOM_UTF8)
    _cache_file[filename].write("%s\n" % msg)
    _cache_file[filename].flush()

if __name__ == '__main__':
    #laok.lktest_run('')#catch_except = True
    test= read_csv_lktest()


    filename = "totest.txt"
    for key,value in test.items():
        value_new = ';'.join(value).replace('"',',').replace(';',',,')
        write_file(filename,key+';'+value_new)

