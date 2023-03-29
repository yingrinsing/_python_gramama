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
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # nums_str = [str(i) for i in nums]
        # print(nums_str)
        # compare = lambda x, y: 1 if x + y < y + x else -1
        def compare(x,y):
            print("x=%s,y=%s" %(x,y))
            # return 1 if x + y < y + x else -1
            return 1 if x<y else -1
        nums.sort(key=cmp_to_key(compare))
        print(nums)
        # return "".join(nums)

if __name__ == '__main__':
    so = Solution()
    nums = [3, 30, 34, 5, 9]
    so.largestNumber(nums)