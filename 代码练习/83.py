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
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def initList(self, data):
        # 判断是否为空
        if len(data) == 0:
            return
        else:
            # 创建头结点
            self.head = ListNode(data[0])
            # 头结点
            r = self.head
            # 指针
            p = self.head
            # 逐个为 data 内的数据创建结点, 建立链表
            for i in data[1:]:
                node = ListNode(i)
                p.next = node
                p = p.next
            return r

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        while tmp and tmp.next:
            if tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return head

if __name__ == '__main__':
    nums = [1,1,2,3,3]
    so = Solution()
    head = so.initList(nums)
    res = so.deleteDuplicates(head)
    while res:
        print(res.val)
        res = res.next

    from collections import Counter
    s = "abccccdd"
    dic = Counter(s)
    for key,value in dic.items():
        print(value)
    print(dic)