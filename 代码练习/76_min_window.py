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
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         start = 0
#         n = len(s)
#         min_len = 0
#         min_str = ""
#         cur_s_list = []
#         cur_t_list = list(t)
#         for i in range(n):
#             print(s[i])
#             if s[i] in cur_t_list:
#                 cur_t_list.remove(s[i])
#             while s[i] in t and s[i] in cur_s_list or (s[start] not in t and s[i] not in cur_s_list):
#                 cur_s_list.remove(s[start])
#                 if s[start] in t and s[start] != s[i]:
#                     cur_t_list.append(s[start])
#                 start+=1
#             cur_s_list.append(s[i])
#             if len(cur_t_list) == 0:
#                 if min_len == 0 or len(cur_s_list) < min_len:
#                     min_len = len(cur_s_list)
#                     min_str = "".join(cur_s_list)
#         if len(cur_t_list)!=0:
#             return ""
#         return min_str

class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0
        end = 0
        min_len = float("inf")
        counter = len(t)
        res = ""
        while end < len(s):
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res


if __name__ == '__main__':
    so = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    output = so.minWindow(s,t)
    print("结果是"+output)
    import collections
    cnt = collections.Counter(t)
    print(cnt)