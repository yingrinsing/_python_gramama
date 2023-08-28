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
from collections import Counter

if __name__ == '__main__':
    a = [1,3,4,2,1,5]
    b = Counter(a)
    print(b)

    print(b.most_common(1)[0][1])