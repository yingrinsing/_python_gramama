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
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        nums = []
        for i in range(n):
            print(ord(s[i]), ord(t[i]))
            nums[i] = ord(s[i]) - ord(t[i])

        max_len,sum_num=0,0
        start = 0
        for end in range(n):
            sum_num+=nums[end]
            if sum_num<=maxCost:
                max_len=max(max_len,end-start+1)
            while sum_num>maxCost:
                sum_num-=nums[start]
                start+=1
        return max_len

if __name__ == '__main__':
    so=Solution()
    so.equalSubstring("abcd","bcdf",3)