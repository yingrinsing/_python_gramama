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
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        t = strs[0]
        n = len(t)
        for i in range(n):
            for s in strs[1:]:
                if len(s) == i or s[i] != t[i]:
                    return t[0:i]
        return t


if __name__ == '__main__':
    so=Solution()
    strs = ["ab", "a"]
    print(so.longestCommonPrefix(strs))
    a = [1]
    b = [2]
    print(a+b)
