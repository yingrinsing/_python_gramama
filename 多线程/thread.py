#! /usr/bin/env python
# -*- coding: utf-8 -*-


import threading

"""
Created on 2018-1-25

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


def thread_func(num):
    global total, mutex  
      
    # 打印线程名  
    print threading.currentThread().getName()  
   
    for x in xrange(0, int(num)):  
        # 取得锁  
        mutex.acquire()  
        total = total + 1  
        # 释放锁  
        mutex.release()  
   
def main(num):  
    # 定义全局变量
    global total, mutex  
    total = 0  
    # 创建锁  
    mutex = threading.Lock()  
      
    # 定义线程池
    threads = []  
    # 先创建线程对象  
    for x in xrange(0, num):  
        threads.append(threading.Thread(target=thread_func, args=(100,)))
    # 启动所有线程  
    for t in threads:  
        t.start()  
    # 主线程中等待所有子线程退出  
    for t in threads:  
        t.join()    
          
    # 打印执行结果  
    print total  
   
   
if __name__ == '__main__':  
    # 创建40个线程  
    main(40)  