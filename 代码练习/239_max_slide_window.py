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
import heapq
from typing import List
from collections import deque

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         # 注意 Python 默认的优先队列是小根堆
#         q = [(-nums[i], i) for i in range(k)]
#         heapq.heapify(q)
#
#         ans = [-q[0][0]]
#         for i in range(k, n):
#             heapq.heappush(q, (-nums[i], i))
#             while q[0][1] <= i - k:
#                 heapq.heappop(q)
#             ans.append(-q[0][0])
#
#         return ans

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            print(q)
            while q[0] <= i - k:
                q.popleft()
            print(q)
            ans.append(nums[q[0]])

        return ans

if __name__ == '__main__':
    so=Solution()
    nums = [1, 9, -1, -3, 5, 3, 6, 7]
    k = 3
    print(so.maxSlidingWindow(nums,k))
    # print(nums[-1])