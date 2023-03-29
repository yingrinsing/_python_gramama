#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""

# ===============================================================================
# 
# ===============================================================================

def climbStairs(n: int) -> int:
    a = b = 1
    for i in range(2, n + 1):
        a = b
        b = a+b
        # a, b = b, a + b
        print(a,b)
    return b

if __name__ == '__main__':
    s = climbStairs(5)