#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-10-9

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
import re
import os
from codecs import open
import sys
reload(sys)  
sys.setdefaultencoding("utf-8")
import emoji
#===============================================================================
# 
#===============================================================================
#<module 're' from 'D:\InstallSoftware\Anaconda2\lib\re.pyc'>,<type 'module'>正则表达式标准库regular expression
#attribute---->
    #DEBUG[<type 'int'>] [128]
    #DOTALL[<type 'int'>] [16]
    #I[<type 'int'>] [2]
    #IGNORECASE[<type 'int'>] [2]
    #L[<type 'int'>] [4]
    #LOCALE[<type 'int'>] [4]
    #M[<type 'int'>] [8]
    #MULTILINE[<type 'int'>] [8]
    #S[<type 'int'>] [16]
    #Scanner[<type 'classobj'>] [re.Scanner]
    #T[<type 'int'>] [1]
    #TEMPLATE[<type 'int'>] [1]
    #U[<type 'int'>] [32]
    #UNICODE[<type 'int'>] [32]
    #VERBOSE[<type 'int'>] [64]
    #X[<type 'int'>] [64]
    #copy_reg[<type 'module'>] [<module 'copy_reg' from 'D:\InstallSoftware\Anaconda2\lib\copy_reg.pyc'>]
    #error[<type 'type'>] [<class 'sre_constants.error'>]
    #sre_compile[<type 'module'>] [<module 'sre_compile' from 'D:\InstallSoftware\Anaconda2\lib\sre_compile.pyc'>]
    #sre_parse[<type 'module'>] [<module 'sre_parse' from 'D:\InstallSoftware\Anaconda2\lib\sre_parse.pyc'>]
    #sys[<type 'module'>] [<module 'sys' (built-in)>]
#funcs/method---->
    #compile(pattern, flags=0) [Compile a regular expression pattern, returning a pattern object.]
    #escape(pattern) [Escape all non-alphanumeric characters in pattern.]
    #findall(pattern, string, flags=0) [Return a list of all non-overlapping matches in the string.]
    #finditer(pattern, string, flags=0) [Return an iterator over all non-overlapping matches in the]
    #match(pattern, string, flags=0) [Try to apply the pattern at the start of the string, returning]
    #purge() [Clear the regular expression cache]
    #search(pattern, string, flags=0) [Scan through string looking for a match to the pattern, returning]
    #split(pattern, string, maxsplit=0, flags=0) [Split the source string by the occurrences of the pattern,]
    #sub(pattern, repl, string, count=0, flags=0) [Return the string obtained by replacing the leftmost]
    #subn(pattern, repl, string, count=0, flags=0) [Return a 2-tuple containing (new_string, number).]
    #template(pattern, flags=0) [Compile a template pattern, returning a pattern object]
    #http://www.cnblogs.com/vamei/archive/2012/08/31/2661870.html
def sub_function():
    s = 'indicators:=1,0,0,0'
    pat = '^indicators:=([0-9]+,){3}([0-9])$'
    new_pat ='indicators:=2,0,0,0'
    news=re.sub(pat, new_pat, s)                       # 正则部分替换，将s中的所有符合pat的全部替换为newpat，newpat也可以是函数
    print news


def search():
    s = ('600875.SH','300875.SH')
#     pattern = '.[A-Za-z]+'
#     if re.search(pattern,s):
#         print 'success'
    s = [re.sub('.[a-zA-Z]+','',n) if re.search('.[A-Za-z]+',n) else n for n in s]
    print s


def findall():
#     s = 'n1_s1_data_exception'
#     s1= re.findall('[a-z]\d{1,}_[a-z]\d{1,}', s)[0]
    #t="<font color='red'>南京</font><font color='red'>二手房</font>每周日均<font color='red'>销量</font>"
    #t= "关于控股股东进行股票质押式<font color='red'>回购交易</font>的公告"
    t_unicode = t.decode('UTF-8')
    #t1 = re.findall(u"<font color='red'>[\u4e00-\u9fa5|a-z|A-Z]+</font>", t_unicode)
    t1 = re.findall(u"<font color='red'>(.+?)</font>", t_unicode)
    print ''.join(t1)
    for i in t1:
        print i


def chinese():
    source=u"数据结构模版----单链表SimpleLinkList[带头结点&&面向对象设计思想](C语言实现)"
    temp=source.decode('utf8')
    print "同时匹配中文英文"
    print "--------------------------"
    xx=u"([\w\W\u4e00-\u9fff]+)"
    pattern = re.compile(xx)
    results = pattern.findall(temp)
    for result in results:
        print result
    print "--------------------------"
    print
    print
    print "只匹配中文"
    print "--------------------------"
    xx      =   u"([\u4e00-\u9fff]+)"
    pattern =   re.compile(xx)
    results =   pattern.findall(temp)

    for result in results:
        print result
    print "--------------------------"


def ppl():
    # s = 'n1_s1_data_exception'
    # s1= re.findall('[a-z]\d{1,}_[a-z]\d{1,}', s)[0]
    #t="<font color='red'>南京</font><font color='red'>二手房</font>每周日均<font color='red'>销量</font>"
    t= "白酒/n/证券_指数_地域_中国&&概念&&行业 | 销量/n/通用_指标_行业&&通用_指标&&通用_指标_公司 | 走势/n/ | ，/n/人物_研报作者 | 陈莉/n/人物_企业_监事&&人物_企业_高管&&人物_企业_未分类&&人物_企业_法人&&人物_企业_董事&&人物_研报作者 | "
    t_unicode = t.decode('UTF-8')
    #t1 = re.findall(u"<font color='red'>[\u4e00-\u9fa5|a-z|A-Z]+</font>", t_unicode)
    t1 = re.findall(u"[\u4e00-\u9fa5|a-z|A-Z|0-9]+/n", t_unicode)
    print ''.join(t1)
    for i in t1:
        print i


def read_file(filename, encode=None):
    """
        读取文件，以list格式返回所有行数据.\n
        return list
                            例子：
        | ${list}= | read_file | ***.txt | UTF-8 |

    """
    with open(filename = filename , mode = 'r' ,encoding = encode) as f:
        _query = {line.rstrip('\r\n') for line in f}
        return list(_query)

def filter_emoji(desstr,restr=''):
    try:
        # co = re.compile(u'('
        #                 u'?:[\uD83C\uDF00-\uD83D\uDDFF]|[\uD83E\uDD00-\uD83E\uDDFF]|[\uD83D\uDE00-\uD83D\uDE4F]|[\uD83D\uDE80-\uD83D\uDEFF]|[\u2600-\u26FF]\uFE0F?|[\u2700-\u27BF]\uFE0F?|\u24C2\uFE0F?|[\uD83C\uDDE6-\uD83C\uDDFF]{1,2}|[\uD83C\uDD70\uD83C\uDD71\uD83C\uDD7E\uD83C\uDD7F\uD83C\uDD8E\uD83C\uDD91-\uD83C\uDD9A]\uFE0F?|[\u0023\u002A\u0030-\u0039]\uFE0F?\u20E3|[\u2194-\u2199\u21A9-\u21AA]\uFE0F?|[\u2B05-\u2B07\u2B1B\u2B1C\u2B50\u2B55]\uFE0F?|[\u2934\u2935]\uFE0F?|[\u3030\u303D]\uFE0F?|[\u3297\u3299]\uFE0F?|[\uD83C\uDE01\uD83C\uDE02\uD83C\uDE1A\uD83C\uDE2F\uD83C\uDE32-\uD83C\uDE3A\uD83C\uDE50\uD83C\uDE51]\uFE0F?|[\u203C\u2049]\uFE0F?|[\u25AA\u25AB\u25B6\u25C0\u25FB-\u25FE]\uFE0F?|[\u00A9\u00AE]\uFE0F?|[\u2122\u2139]\uFE0F?|\uD83C\uDC04\uFE0F?|\uD83C\uDCCF\uFE0F?|[\u231A\u231B\u2328\u23CF\u23E9-\u23F3\u23F8-\u23FA]\uFE0F]?)+',
        #                           re.UNICODE)
        # co = re.compile(u'[\uD83C\uDF00-\uD83D\uDDFF]+',re.UNICODE)
        co = re.compile(u'[^\u4E00-\u9FA50-9_,.;\'\"?，。、？‘’“”：；《》，<>!！%%#@……]+$')
    except re.error as e:
        # Narrow UCS-2 build
        print(e)
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')

    pe = co.findall(desstr)
    print(pe)

    return co.sub(restr, desstr)

# def filter_emoji(desstr,restr=''):
#     '''
#     过滤表情
#     '''
#     try:
#         co = re.compile(u'[\U00010000-\U0010ffff]')
#     except re.error:
#         co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
#     return co.sub(restr, desstr)

def filter_emoj(text):
    try:
        # Wide UCS-4 build
        myre = re.compile(u'['
                          u'\U0001F300-\U0001F64F'
                          u'\U0001F680-\U0001F6FF'
                          u'\u2600-\u2B55'
                          u'\u23cf'
                          u'\u23e9'
                          u'\u231a'
                          u'\u3030'
                          u'\ufe0f'
                          u"\U0001F600-\U0001F64F"
                           u"\U0001F300-\U0001F5FF"
                            u'\U00010000-\U0010ffff'
                           u'\U0001F1E0-\U0001F1FF'
                           u'\U00002702-\U000027B0]+',
                          re.UNICODE)
    except re.error as e:
        # Narrow UCS-2 build
        print(e)
        myre = re.compile(u'('
                                  u'\ud83c[\udf00-\udfff]|'
                                  u'\ud83d[\udc00-\ude4f]|'
                                  u'\uD83D[\uDE80-\uDEFF]|'
                                  u"(\ud83d[\ude00-\ude4f])|" 
                                  u'[\u2600-\u2B55]|'
                                  u'[\u23cf]|'
                                  u'[\u1f918]|'
                                    u'[\u23e9]|'
                                  u'[\u231a]|'
                                  u'[\u3030]|'
                                  u'[\ufe0f]|'
                                  u'\uD83D[\uDE00-\uDE4F]|'
                                  u'\uD83C[\uDDE0-\uDDFF]|'
                                u'[\u2702-\u27B0]|'
                                  u'\uD83D[\uDC00-\uDDFF])+',
                                  re.UNICODE)
    text=myre.sub('', text)
    # print(text)
    return text

'''
正则表达式匹配空行

测试所用的编辑器:notepad++

^(\s*)\r\n

根据文档格式(windows, mac, linux行尾符)不同 将其中的\r\n替换成不同行尾符

windows: ^(\s*)\r\n

linux: ^(\s*)\n

mac: ^(\s*)\n (mac 也是一种类linux系统)
'''



if __name__ == '__main__':
    tt = '你好[Respect]'
    emoji_tt = emoji.emojize(tt)
    print(emoji_tt)
    t = filter_emoji(emoji_tt)
    print(t)

    t2 = re.sub('[^\\u4E00-\\u9FA50-9_,.;\'\"?，。、？‘’“”：；《》，<>!！%%#@……]+$', '','你好[Respect]')
    print(t2)
    # slashUStr = "\\u0063\\u0072\\u0069\\u0066\\u0061\\u006E\\u0020\\u5728\\u8DEF\\u4E0A"
    # decodedUniChars = slashUStr.decode("unicode-escape")
    # print "decodedUniChars=", decodedUniChars
    # encodeUniChars = tt.encode("unicode-escape")
    # print "encodeUniChars", encodeUniChars