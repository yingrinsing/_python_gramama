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
if __name__ == '__main__':
    pro = product('ABCD', repeat=2)
    per = permutations('ABCD', 2)
    com = combinations('ABCD', 2)
    com_r = combinations_with_replacement('ABCD', 2)
    print([x for x in pro])
    print([x for x in per])
    print([x for x in com])
    print([x for x in com_r])