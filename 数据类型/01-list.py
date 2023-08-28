#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-9-26

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


#===============================================================================
# 
#===============================================================================
#<type 'list'>
#builtin-method---->
    #append [<type 'builtin_function_or_method'>] [L.append(object) -- append object to end]
    #count [<type 'builtin_function_or_method'>] [L.count(value) -> integer -- return number of occurrences of value]
    #extend [<type 'builtin_function_or_method'>] [L.extend(iterable) -- extend list by appending elements from the iterable]
    #index [<type 'builtin_function_or_method'>] [L.index(value, [start, [stop]]) -> integer -- return first index of value.  Raises ValueError if the value is not present.]
    #insert [<type 'builtin_function_or_method'>] [L.insert(index, object) -- insert object before index]
    #pop [<type 'builtin_function_or_method'>] [L.pop([index]) -> item -- remove and return item at index (default last).  Raises IndexError if list is empty or index is out of range.]
    #remove [<type 'builtin_function_or_method'>] [L.remove(value) -- remove first occurrence of value.  Raises ValueError if the value is not present.]
    #reverse [<type 'builtin_function_or_method'>] [L.reverse() -- reverse *IN PLACE*]
    #sort [<type 'builtin_function_or_method'>] [L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;  cmp(x, y) -> -1, 0, 1]
def interaction():
    list1 = [1,2,4,6,8]
    list2 = [1,2,3,5,7]
    interaction1 = list(set(list1).intersection(set(list2)))
    interaction2 = [x for x in list1 if x in list2]

    
    
def union():
    list1 = [1,2,4,6,8]
    list2 = [1,2,3,5,7]
    union1 = list(set(list1).union(set(list2)))
    #union2 = list2.extend([v for v in list1])
    list1.extend(list2)

def difference():
    list1 = [1,2,4,6,8]
    list2 = [1,2,3,5,7]
    #list1和list2均不同的元素
    d1 = list(set(list1) ^ set(list2))

    #list1有list2没有
    d2 = list(set(list1).difference(set(list2))) 

    d3 = [v for v in list1 if v not in list2]



def multi_same_string():
    num_list = [1 for i in range(5)]


def sort1():
    list1 = [1,2,7,6,8]
    list1.sort()

def sum_dict1(a,b):
    temp = dict()
    # python3,dict_keys类似set； | 并集
    for key in a.keys()| b.keys():
        # temp[key] = sum([d.get(key, 0) for d in (a, b)])
        temp[key] = a.get(key, 0) + b.get(key, 0)
    return temp
def sum_dict2(a,b):
    temp = dict()
    # python3,dict_keys类似set； | 并集
    for key in a.keys()| b.keys():
        temp[key] = sum([d.get(key, 0) for d in (a, b)])
        # temp[key] = a.get(key, 0) + b.get(key, 0)
    return temp

def test():
    #python3使用reduce需要先导入
    from functools import reduce
    #[a,b,c]列表中的参数可以2个也可以多个，自己尝试。
    a = {'a': 1, 'b': 2, 'c': 3}
    b = {'a':1,'b':3,'d':4}
    c = {'g':3,'f':5,'a':10}
    print(reduce(sum_dict1,[a,b,c]))
    print(reduce(sum_dict2,[a,b,c]))

if __name__ == '__main__':
    #laok.lktest_run()#catch_except = True
    #interaction()
    #union()
    #difference()
    #multi_same_string()
    #sort1()


    test()
