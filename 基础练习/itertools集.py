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
from itertools import combinations,permutations,product,combinations_with_replacement

if __name__ == '__main__':
    pro = product('ABCD', repeat=2)
    per = permutations('ABCD', 2)
    com = combinations('ABCD', 2)
    com_r = combinations_with_replacement('ABCD', 2)
    print([x for x in pro])
    print([x for x in per])
    print([x for x in com])
    print([x for x in com_r])