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
    def longestOnes(self, nums, k):
        max_len, hash_map = 0, {}

        start = 0
        for end in range(len(nums)):
            hash_map[nums[end]] = hash_map.get(nums[end], 0) + 1
            print(hash_map)
            if hash_map.get(0, 0) <= k:
                max_len = max(max_len, end - start + 1)

            while hash_map.get(0, 0) > k:
                hash_map[nums[start]] -= 1
                start += 1
                print(start)
                print('ok')
                print(hash_map)
        return max_len


if __name__ == '__main__':
    so = Solution()
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    print(so.longestOnes(nums,2))