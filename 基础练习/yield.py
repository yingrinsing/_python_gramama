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
aa = [[(55736,)], [(55739,)], [(55740,), (55801,)], [(55748,)], [(55783,), (55786,), (55787,), (55788,)],[(55817,), (55821,)], [(55818,)]]

def getelement(aa):
    for elem in aa:
       if type(elem) == type([]):
          for element in elem:
             yield element
       else:
          yield elem


if __name__ == '__main__':
    A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
    print(A0)