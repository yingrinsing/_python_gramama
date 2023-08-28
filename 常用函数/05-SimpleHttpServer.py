#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-11-3

@author: laok@ArgusTech
@email:  1306743659@qq.com
@copyright: Apache License, Version 2.0
"""
import SimpleHTTPServer
import sys
import socket, webbrowser
#===============================================================================
# 
#===============================================================================
#设置默认端口
if len(sys.argv) == 1:
    sys.argv.append('80')

#打开网页

print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))
url = "http://%s" % socket.gethostbyname(socket.gethostname())
webbrowser.open(url)

#启动服务器
SimpleHTTPServer.test()