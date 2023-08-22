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
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        dic = Counter(nums)
        max = 0
        for key,values in dic.items():
            if values>max:
                max=values
        return li[0][0]

if __name__ == '__main__':
    so = Solution()
    nums = [3, 3, 34, 5, 9]
    print(so.majorityElement(nums))