#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-9-29

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


def safe_float1(str):
    try:
        retval =  float(str)
    except ValueError:
        retval = "could not convert non-number to float"
    except TypeError:
        retval = "float() argument must be a string or a number"
    return retval


def safe_float2(str):
    try:
        retval =  float(str)
    except (ValueError,TypeError):
        retval = "must be a string or a number"
    return retval


def safe_float_All(str):
    try:
        retval =  float(str)
    except Exception:
        retval = "All Exception:must be a string or a number"
    return retval
    

if __name__ == '__main__':
    str1 = safe_float1(123)
    print(str1)
    str2 = safe_float1('123')
    print(str2)
    str3 = safe_float1('abc')
    print(str3)
    str4 = safe_float1(['abc', 1])
    print(str4)
    
    str5 = safe_float2('abc')
    print(str5)
    str6 = safe_float2(['abc',1])
    print(str6)
    
    str7 = safe_float_All('abc')
    print(str7)
    str8 = safe_float_All(['abc',1])
    print(str8)