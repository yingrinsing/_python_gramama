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
    def validIPAddress(self, queryIP: str) -> str:
        if "." in  queryIP:
            q= queryIP.split(".")
            if len(q)!=4:
                return "Neither"
            for x in q:
                try:
                    if x.startswith("0") and len(x)!=1:
                        return "Neither"
                    if int(x)<0 or int(x)>255:
                        return "Neither"
                except Exception as e:
                    print(e)
                    return "Neither"
            return "IPv4"
        elif ":" in queryIP:
            q= queryIP.split(":")
            if len(q)!=8:
                return "Neither"
            for x in q:
                if x=="0":
                    continue
                if len(x)!=4:
                    return "Neither"
                else:
                    for xx in x:
                        # xx = xx.lower()
                        if xx not in "0123456789abcdefABCDEF":
                            return "Neither"
            return "IPv6"
        else:
            return "Neither"

if __name__ == '__main__':
    so = Solution()
    print(so.validIPAddress(queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"))