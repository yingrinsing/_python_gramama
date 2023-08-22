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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        s=0
        ans = []
        for k in range(n):
            if nums[k]>0:break
            if k>0 and nums[k]==nums[k-1]:continue
            i=k+1
            j=n-1
            while i<j:
                s= nums[k]+nums[i]+nums[j]
                if s<0:
                    i+=1
                    while i<j and nums[i]==nums[i-1]:i+=1
                elif s>0:
                    j-=1
                    while i<j and j<n-1 and nums[j]==nums[j+1]:j-=1
                else:
                    ans.append([nums[k],nums[i],nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i<j and j<n-1 and nums[j] == nums[j + 1]: j -= 1
        return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    so = Solution()
    print(so.threeSum(nums))