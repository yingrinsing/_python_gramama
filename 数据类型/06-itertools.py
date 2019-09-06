#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-11-21

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
import itertools
#===============================================================================
# 
#===============================================================================
#chain[<type 'type'>] [<type 'itertools.chain'>]
    #combinations[<type 'type'>] [<type 'itertools.combinations'>]
    #combinations_with_replacement[<type 'type'>] [<type 'itertools.combinations_with_replacement'>]
    #compress[<type 'type'>] [<type 'itertools.compress'>]
    #count[<type 'type'>] [<type 'itertools.count'>]
    #cycle[<type 'type'>] [<type 'itertools.cycle'>]
    #dropwhile[<type 'type'>] [<type 'itertools.dropwhile'>]
    #groupby[<type 'type'>] [<type 'itertools.groupby'>]
    #ifilter[<type 'type'>] [<type 'itertools.ifilter'>]
    #ifilterfalse[<type 'type'>] [<type 'itertools.ifilterfalse'>]
    #imap[<type 'type'>] [<type 'itertools.imap'>]
    #islice[<type 'type'>] [<type 'itertools.islice'>]
    #izip[<type 'type'>] [<type 'itertools.izip'>]
    #izip_longest[<type 'type'>] [<type 'itertools.izip_longest'>]
    #permutations[<type 'type'>] [<type 'itertools.permutations'>]
    #product[<type 'type'>] [<type 'itertools.product'>]
    #repeat[<type 'type'>] [<type 'itertools.repeat'>]
    #starmap[<type 'type'>] [<type 'itertools.starmap'>]
    #takewhile[<type 'type'>] [<type 'itertools.takewhile'>]
#builtin-method---->
    #tee [<type 'builtin_function_or_method'>] [tee(iterable, n=2) --> tuple of n independent iterators.]
def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def _lktest():
#     obj = itertools
#     laok.dump_description_help(obj)
    llll = list(product(['1','2','3'], ['a','b','c'] ,['p','q','r'])) 
    print llll
    
def comb():
    list = [u'\u6362\u624b\u7387', u'\u5e02\u9500\u7387', u'\u5e02\u73b0\u7387', u'\u5e02\u51c0\u7387\uff08TTM\uff09', u'\u5e02\u76c8\u7387', u'\u5e02\u76c8\u7387\uff08TTM\uff09', u'\u5e02\u51c0\u7387', u'\u5e02\u9500\u7387\uff08TTM\uff09', u'\u6bcf\u65e5\u80a1\u4ef7', u'\u5e02\u73b0\u7387\uff08TTM\uff09']
    comb = itertools.combinations(list, 1)
    while True:
        try:
            next = comb.next()
            print next
        except StopIteration:
            break

    
def comb1():  
    test_data = ['a', 'a', 'a', 'b']
    for i in itertools.combinations(test_data, 2):
        print i
        laok.dump_description_help(i)
if __name__ == '__main__':
    #laok.lktest_run()#catch_except = True
    
    comb()