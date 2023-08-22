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
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[k] = nums1[m - 1]
                m -= 1
            else:
                nums1[k] = nums2[n - 1]
                n -= 1
            k -= 1
        nums1[:n] = nums2[:n]

if __name__ == '__main__':
    so=Solution()
    nums1 = [1, 2, 3]
    m = 3
    nums2 = [2, 1, 3]
    n = 3
    # so.merge(nums1,m,nums2,n)
    print(nums1==nums2)
