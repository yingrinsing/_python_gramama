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
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(begin,path,target):
            if target==0:
                res.append(path)
                return
            # if begin==size:
            #     return

            for i in range(begin,size):
                reduce = target-candidates[i]
                if reduce<0:
                    return
                if i>begin and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1,path+[candidates[i]],reduce)

        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        res = []
        dfs(0,[],target)
        return res

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        ans = 0
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # dp = [[0]*(n+1)]*(m+1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
                    print(dp)
        return ans

if __name__ == '__main__':
    candidates = [1,1]
    target = 3
    so = Solution()
    # print(so.combinationSum2(candidates,target))
    nums = [1,2,4]
    nums2 = [1,0,0,1,1]
    import itertools
    res = []
    for i in range(len(nums) + 1):
        for tmp in itertools.combinations(nums, i):
            print(tmp)
            res.append(tmp)
            print(res)