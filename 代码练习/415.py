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
    def addStrings(self, num1: str, num2: str) -> str:
        m,n = len(num1),len(num2)
        carry=0
        tmp=0
        res=[]
        max_size = max(m,n)
        for k in range(max_size):
            num1_cur = 0 if k>=m else int(num1[-1-k])
            num2_cur = 0 if k>=n else int(num2[-1-k])
            tmp=num1_cur+num2_cur+carry
            carry=tmp//10
            if k==max_size-1:
                res.insert(0, str(tmp))
            else:
                res.insert(0,str(tmp%10))
        return "".join(res)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        long = len(num1) if len(num1) > len(num2) else len(num2)
        num1 = "0" * (long - len(num1)) + num1
        num2 = "0" * (long - len(num2)) + num2
        ans = ""
        add = 0
        for i in range( long - 1, -1, -1):
            res = add + int(num1[i]) + int(num2[i])
            if res >=10:
                add = 1
                res -= 10
            else:
                add = 0
            ans += str(res)
        if add:
            ans += str(add)
        return(ans[::-1])

if __name__ == '__main__':
    so = Solution()
    num1 = "9"
    num2 = "99"
    print(so.addStrings(num1,num2))