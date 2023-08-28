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
#{},<type 'dict'>
#builtin-method---->
    #clear [<type 'builtin_function_or_method'>] [D.clear() -> None.  Remove all items from D.]
    #copy [<type 'builtin_function_or_method'>] [D.copy() -> a shallow copy of D]
    #fromkeys [<type 'builtin_function_or_method'>] [dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.  v defaults to None.]
    #get [<type 'builtin_function_or_method'>] [D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.]
    #has_key [<type 'builtin_function_or_method'>] [D.has_key(k) -> True if D has a key k, else False]
    #items [<type 'builtin_function_or_method'>] [D.items() -> list of D's (key, value) pairs, as 2-tuples]
    #iteritems [<type 'builtin_function_or_method'>] [D.iteritems() -> an iterator over the (key, value) items of D]
    #iterkeys [<type 'builtin_function_or_method'>] [D.iterkeys() -> an iterator over the keys of D]
    #itervalues [<type 'builtin_function_or_method'>] [D.itervalues() -> an iterator over the values of D]
    #keys [<type 'builtin_function_or_method'>] [D.keys() -> list of D's keys]
    #pop [<type 'builtin_function_or_method'>] [D.pop(k[,d]) -> v, remove specified key and return the corresponding value.  If key is not found, d is returned if given, otherwise KeyError is raised]
    #popitem [<type 'builtin_function_or_method'>] [D.popitem() -> (k, v), remove and return some (key, value) pair as a  2-tuple; but raise KeyError if D is empty.]
    #setdefault [<type 'builtin_function_or_method'>] [D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D]
    #update [<type 'builtin_function_or_method'>] [D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.  If E present and has a .keys() method, does:     for k in E: D[k] = E[k]  If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v  In either case, this is followed by: for k in F: D[k] = F[k]]
    #values [<type 'builtin_function_or_method'>] [D.values() -> list of D's values]
    #viewitems [<type 'builtin_function_or_method'>] [D.viewitems() -> a set-like object providing a view on D's items]
    #viewkeys [<type 'builtin_function_or_method'>] [D.viewkeys() -> a set-like object providing a view on D's keys]
    #viewvalues [<type 'builtin_function_or_method'>] [D.viewvalues() -> an object providing a view on D's values]

def sort_list_dict():
    info = [{"name": "张三", "age": 4}, {"name": "李四", "age": 5}, {"name": "王五", "age": 1}]
    v = sorted(info, key=lambda s: s["age"], reverse=True)
    print(v)

def sort_dict():
    dict_data = {'form': 2, 'table': 1, 'file': 3}
    v1 = sorted(dict_data.items(), key=lambda x:x[0])
    print(v1)
    v2 = sorted(dict_data.items(), key=lambda x: x[1])
    print(v2)


if __name__ == '__main__':
    dict1 = {}
    print(dict1)
    dict2 = {
        "name": "wangning",
        "age": 13
    }
    dict1.update(dict2)
    print(dict1)
    print(dict2.get("sex", "未知"))
    dict2.popitem()
    print(dict2)
    dict2.setdefault("name","guying")
    print(dict2)
    dict3 = dict.fromkeys(["name","age","sex"], "")
    print(dict3)

    sort_dict()
    sort_list_dict()

