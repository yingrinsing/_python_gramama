#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime  
import os  
import threading

"""
Created on 2018-1-25

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
# Filename: put_files_hdfs.py  
# 让多条命令并发执行,如让多条scp,ftp,hdfs上传命令并发执行,提高程序运行效率  
"""


def exec_cmd(cmd):
    try:  
        print "命令%s开始运行%s" % (cmd,datetime.datetime.now())  
        os.system(cmd)  
        print "命令%s结束运行%s" % (cmd,datetime.datetime.now())  
    except Exception, e:  
        print '%s\t 运行失败,失败原因\r\n%s' % (cmd,e)  


if __name__ == '__main__':  
    # 需要执行的命令列表  
    cmds = ['ls', 'pwd']
      
    # 线程池
    threads = []  
      
    print "程序开始运行%s" % datetime.datetime.now()  
  
    for cmd in cmds:  
        th = threading.Thread(target=exec_cmd, args=(cmd,))
        th.start()  
        threads.append(th)  
           
    # 等待线程运行完毕  
    for th in threads:  
        th.join()  
           
    print "程序结束运行%s" % datetime.datetime.now()