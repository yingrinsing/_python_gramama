#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-9-26

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
#===============================================================================
# 
#===============================================================================
#<type 'set'>,<type 'type'>
#funcs/method---->
    #__init__(...) ==>x.__init__(...) initializes x; see help(type(x)) for signature
    #add(...) ==>Add an element to a set.
    #clear(...) ==>Remove all elements from this set.
    #copy(...) ==>Return a shallow copy of a set.
    #difference(...) ==>Return the difference of two or more sets as a new set.
    #difference_update(...) ==>Remove all elements of another set from this set.
    #discard(...) ==>Remove an element from a set if it is a member.
    #intersection(...) ==>Return the intersection of two or more sets as a new set.
    #intersection_update(...) ==>Update a set with the intersection of itself and another.
    #isdisjoint(...) ==>Return True if two sets have a null intersection.
    #issubset(...) ==>Report whether another set contains this set.
    #issuperset(...) ==>Report whether this set contains another set.
    #pop(...) ==>Remove and return an arbitrary set element.
    #remove(...) ==>Remove an element from a set; it must be a member.
    #symmetric_difference(...) ==>Return the symmetric difference of two sets as a new set.
    #symmetric_difference_update(...) ==>Update a set with the symmetric difference of itself and another.
    #union(...) ==>Return the union of sets as a new set.
    #update(...) ==>Update a set with the union of itself and others.
# set()和 frozenset()工厂函数分别用来生成可变和不可变的集合


def _lktest():
    x = set("jihite")
    print(x)
    y = set(['d', 'i', 'm', 'i', 't', 'e'])
    y.add("a")
    print(y)
    laok.dump_description_help(unicode)


if __name__ == '__main__':
    laok.lktest_run()#catch_except = True
    a = set([])
    data_list = ['1','1']
    y = len(list(set(data_list)))
    print(y)
    assert len(data_list) != len(set(data_list))