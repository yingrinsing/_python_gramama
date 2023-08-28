#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-10-11

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
import time
#===============================================================================
# 
#===============================================================================
#<module 'time' (built-in)>,<type 'module'>
#attribute---->
    #accept2dyear[<type 'int'>] [1]
    #altzone[<type 'int'>] [-32400]
    #daylight[<type 'int'>] [0]
    #struct_time[<type 'type'>] [<type 'time.struct_time'>]
    #timezone[<type 'int'>] [-28800]
    #tzname[<type 'tuple'>] [('\xd6\xd0\xb9\xfa\xb1\xea\xd7\xbc\xca\xb1\xbc\xe4', '\xd6\xd0\xb9\xfa\xcf\xc4\xc1\xee\xca\xb1')]
#builtin-method---->
    #asctime [<type 'builtin_function_or_method'>] [asctime([tuple]) -> string    Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.  When the time tuple is not present, current time as returned by localtime()  is used.]
    #clock [<type 'builtin_function_or_method'>] [clock() -> floating point number    Return the CPU time or real time since the start of the process or since  the first call to clock().  This has as much precision as the system  records.]
    #ctime [<type 'builtin_function_or_method'>] [ctime(seconds) -> string    Convert a time in seconds since the Epoch to a string in local time.  This is equivalent to asctime(localtime(seconds)). When the time tuple is  not present, current time as returned by localtime() is used.]
    #gmtime [<type 'builtin_function_or_method'>] [gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,                         tm_sec, tm_wday, tm_yday, tm_isdst)    Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.  GMT).  When 'seconds' is not passed in, convert the current time instead.]
    #localtime [<type 'builtin_function_or_method'>] [localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,                            tm_sec,tm_wday,tm_yday,tm_isdst)    Convert seconds since the Epoch to a time tuple expressing local time.  When 'seconds' is not passed in, convert the current time instead.]
    #mktime [<type 'builtin_function_or_method'>] [mktime(tuple) -> floating point number    Convert a time tuple in local time to seconds since the Epoch.]
    #sleep [<type 'builtin_function_or_method'>] [sleep(seconds)    Delay execution for a given number of seconds.  The argument may be  a floating point number for subsecond precision.]
    #strftime [<type 'builtin_function_or_method'>] [strftime(format[, tuple]) -> string    Convert a time tuple to a string according to a format specification.  See the library reference manual for formatting codes. When the time tuple  is not present, current time as returned by localtime() is used.]
    #strptime [<type 'builtin_function_or_method'>] [strptime(string, format) -> struct_time    Parse a string to a time tuple according to a format specification.  See the library reference manual for formatting codes (same as strftime()).]
    #time [<type 'builtin_function_or_method'>] [time() -> floating point number    Return the current time in seconds since the Epoch.  Fractions of a second may be present if the system clock provides them.]

    
def timeStampToDateTime(timeStamp):    
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)


def dateTimeToTimeStamp(dateTime):   
    # 将其转换为时间数组
    timeArray = time.strptime(dateTime, "%Y-%m-%d %H:%M:%S")
    # 转换为时间戳:
    timeStamp = int(time.mktime(timeArray)) 
    print(timeStamp)


if __name__ == '__main__':
    laok.lktest_run()
    timeStampToDateTime(1506268800)
    dateTimeToTimeStamp("2016-10-09 23:40:00")
    date1 = '2016-10-09 23:40:00'
    print date1[0:10]
