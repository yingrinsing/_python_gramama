#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016-12-11

@author: laok@laok.studio.com
@email:  1306743659@qq.com
@copyright: Apache License,Version 2.0
"""

#===============================================================================
# 
#===============================================================================
#<type 'str'>,<type 'type'>
#funcs/method---->
    #__init__(...) ==>x.__init__(...) initializes x; see help(type(x)) for signature
    #capitalize(...) ==>S.capitalize() -> string
    #center(...) ==>S.center(width[, fillchar]) -> string
    #count(...) ==>S.count(sub[, start[, end]]) -> int
    #decode(...) ==>S.decode([encoding[,errors]]) -> object
    #encode(...) ==>S.encode([encoding[,errors]]) -> object
    #endswith(...) ==>S.endswith(suffix[, start[, end]]) -> bool
    #expandtabs(...) ==>S.expandtabs([tabsize]) -> string
    #find(...) ==>S.find(sub [,start [,end]]) -> int
    #format(...) ==>S.format(*args, **kwargs) -> string
    #index(...) ==>S.index(sub [,start [,end]]) -> int
    #isalnum(...) ==>S.isalnum() -> bool
    #isalpha(...) ==>S.isalpha() -> bool
    #isdigit(...) ==>S.isdigit() -> bool
    #islower(...) ==>S.islower() -> bool
    #isspace(...) ==>S.isspace() -> bool
    #istitle(...) ==>S.istitle() -> bool
    #isupper(...) ==>S.isupper() -> bool
    #join(...) ==>S.join(iterable) -> string
    #ljust(...) ==>S.ljust(width[, fillchar]) -> string
    #lower(...) ==>S.lower() -> string
    #lstrip(...) ==>S.lstrip([chars]) -> string or unicode
    #partition(...) ==>S.partition(sep) -> (head, sep, tail)
    #replace(...) ==>S.replace(old, new[, count]) -> string
    #rfind(...) ==>S.rfind(sub [,start [,end]]) -> int
    #rindex(...) ==>S.rindex(sub [,start [,end]]) -> int
    #rjust(...) ==>S.rjust(width[, fillchar]) -> string
    #rpartition(...) ==>S.rpartition(sep) -> (head, sep, tail)
    #rsplit(...) ==>S.rsplit([sep [,maxsplit]]) -> list of strings
    #rstrip(...) ==>S.rstrip([chars]) -> string or unicode
    #split(...) ==>S.split([sep [,maxsplit]]) -> list of strings
        #当不给split函数传递任何参数时，分隔符sep会采用任意形式的空白字符：
        #空格、tab、换行、回车以及formfeed。maxsplit参数表明要分割得到的list长度。
    #splitlines(...) ==>S.splitlines(keepends=False) -> list of strings
    #startswith(...) ==>S.startswith(prefix[, start[, end]]) -> bool
    #strip(...) ==>S.strip([chars]) -> string or unicode
    #swapcase(...) ==>S.swapcase() -> string
    #title(...) ==>S.title() -> string
    #translate(...) ==>S.translate(table [,deletechars]) -> string
    #upper(...) ==>S.upper() -> string
    #zfill(...) ==>S.zfill(width) -> string

#str.count(sub)       返回：sub在str中出现的次数
#str.find(sub)        返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1
#str.index(sub)       返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误
#str.rfind(sub)       返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1
#str.rindex(sub)      返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误
#str.isalnum()        返回：True， 如果所有的字符都是字母或数字
#str.isalpha()        返回：True，如果所有的字符都是字母
#str.isdigit()        返回：True，如果所有的字符都是数字
#str.istitle()        返回：True，如果所有的词的首字母都是大写
#str.isspace()        返回：True，如果所有的字符都是空格
#str.islower()        返回：True，如果所有的字符都是小写字母
#str.isupper()        返回：True，如果所有的字符都是大写字母
#str.split([sep, [max]])    返回：从左开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.split(',')的方式使用逗号或者其它分割符
#str.rsplit([sep, [max]])   返回：从右开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.rsplit(',')的方式使用逗号或者其它分割符
#str.join(s)                返回：将s中的元素，以str为分割符，合并成为一个字符串。
#str.strip([sub])           返回：去掉字符串开头和结尾的空格。也可以提供参数sub，去掉位于字符串开头和结尾的sub  
#str.replace(sub, new_sub)  返回：用一个新的字符串new_sub替换str中的sub
#str.capitalize()           返回：将str第一个字母大写
#str.lower()                返回：将str全部字母改为小写
#str.upper()                返回：将str全部字母改为大写
#str.swapcase()             返回：将str大写字母改为小写，小写改为大写
#str.title()                返回：将str的每个词(以空格分隔)的首字母大写
#str.center(width)          返回：长度为width的字符串，将原字符串放入该字符串中心，其它空余位置为空格。
#str.ljust(width)           返回：长度为width的字符串，将原字符串左对齐放入该字符串，其它空余位置为空格。
#str.rjust(width)           返回：长度为width的字符串，将原字符串右对齐放入该字符串，其它空余位置为空格。

def _lktest():
    laok.dump_description_help(str)

def zfill_lktestx():
    width = 6
    print 'hell'.zfill(width)

def str_lktest():
    xyz = 123
    strs = str('123'
               '234'
               'sdfs'
               'C%s' % xyz
               )
    print( strs )

def cmp_lktest():
    id1 = 'AN201709150887191248'
    id2 = 'AN201709150887189039'
    print id1 < id2
    print id1 > id2

def combinations_lktest():
    for codes in combinations(stock_codes, stock_count):
        for ins in combinations(indicators, indicator_count):
            pass

def strip_lktest():
    val = '\t xf yz \r\n'
    print repr(val.rstrip())
    print repr(val.lstrip())
    print repr(val.strip())
    
    val = '\t xf yz \n'
    print repr(val.rstrip())
    print repr(val.lstrip())
    print repr(val.strip())
 
    val = '\t xf yz \r'
    print repr(val.rstrip())
    print repr(val.lstrip())
    print repr(val.strip())

def split():
    s=''
    t=s.split('_')   
    print t
    print len(t) 

if __name__ == '__main__':
    #laok.lktest_run()
    split()