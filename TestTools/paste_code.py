# -*- coding: utf-8 -*-
# @Time    : 2019-12-19 20:35
# @Author  : yingrinsing
# @File    : paste_code.py.py

"""

功能说明

"""
# targetUrl
# fromUrl
# utm_source
# utm_media
# utm_campaign
#

import base64
import time
from urllib import parse
import json

def encodeProtocol(target,fromPage):
    print("target "+ target)
    print("from: "+ fromPage)
    dic = {}
    dic["targetUrl"]=target
    dic["fromUrl"]=fromPage

    dic["ctime"]=int(time.time())
    # dic["ctime"] = 1576742400
    jsonData = json.dumps(dic)
    print("-----------------")
    print(jsonData)
    payload = base64.b64encode(jsonData.encode())
    checkSum = crc8(payload)
    payloadStr = bytes.decode(payload)
    resutl = "{a}{b}{c}{d}{e}".format(a="KY",b="01",c=('%04X' % (len(payloadStr))),d=checkSum,e=payloadStr)
    print(resutl)

# 创建Crc映射表
def crcTable(seed=0x07):
    table=[]
    for i in range(0,256):
        res = i
        for j in range(0, 8):
            if(res & 0x80):
                res = ((res<<1) ^ seed) % 256
            else:
                res = (res<<1) % 256
        table.append(res)
    return table

# 计算CRC8
def crc8(data , table=None):
    if(table == None):
        table = crcTable()
    res = 0
    for b in data:
        res = table[((res ^ b) % 256) & 0xFF]
    return '%02X' % res

def main():
    print('-----------------------')
    scheme="kwaiying://web?"
    param = {}
    param["showTopBar"]="true"
    # param["url"]=parse.quote("https://share.kwaiying.com/activity/starface#/index")
    param["url"]="https://share.kwaiying.com/activity/starface#/index"
    param["utm_source"]="wx"
    param["utm_medium"]="cpc"
    param["utm_campaign"]="mxl"
    print(param)
    targetUrl = scheme+parse.urlencode(param)
    print(targetUrl)
    fromUrl = "https://share.kwaiying.com/activity/starface#/index"
    print(encodeProtocol(targetUrl,fromUrl))
    print('-----------------------')

if __name__ == '__main__':
    main()
