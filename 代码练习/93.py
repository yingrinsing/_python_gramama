#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""

# ===============================================================================
# 
# ===============================================================================y
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        r = []
        def restore(count=0, ip='', s=''): # count record split times, ip record ip, s record remaining string
            if count == 4:
                if s == '':
                    r.append(ip[:-1])
                return
            if len(s) > 0:
                restore(count+1, ip+s[0]+'.', s[1:])
            if len(s) > 1 and s[0] != '0':
                restore(count+1, ip+s[:2]+'.', s[2:])
            if len(s) > 2 and s[0] != '0' and int(s[0:3]) < 256:
                restore(count+1, ip+s[:3]+'.', s[3:])
        restore(0, '', s)
        return r


if __name__ == '__main__':
    s = "101"
    so = Solution()
    res = so.restoreIpAddresses(s)
    print(res)
    print(s[0:3])

    a=s[4:]
    print("a is " +a)