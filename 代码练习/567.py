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
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k = len(s1)
        if k > n:
            return False

        from collections import Counter
        counter_dict = Counter(s1)
        need = k

        for end in range(n):
            ch = s2[end]
            if ch in counter_dict:
                if counter_dict[ch] > 0:
                    need -= 1
                counter_dict[ch] -= 1
            start = end - k
            if start >= 0:
                ch = s2[start]
                if ch in counter_dict:  # 刚滑出的字符位于p中
                    if counter_dict[ch] >= 0:  # 此时滑出窗口的字符对need有影响
                        need += 1
                    counter_dict[ch] += 1

            if need == 0:  # 找到了一个满足题意的窗口，其左端点为right-m+1
                # res.append(end-k+1)
                return True
        return False


if __name__ == '__main__':
    so=Solution()
    s1 = "abd"
    s2 = "dibadooo"
    print(so.checkInclusion(s1,s2))
    print(s1[-1::-1])