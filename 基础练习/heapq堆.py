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
# python默认是小顶堆，每个节点都比左右孩子的值小或者相等，取最小值或者最大值适合用堆
"""
heapq.merge(*iterables, key=None, reverse=False)
将多个已排序的输入合并为一个已排序的输出（例如，合并来自多个日志文件的带时间戳的条目）。 返回已排序值的 iterator。

类似于 sorted(itertools.chain(*iterables)) 但返回一个可迭代对象，不会一次性地将数据全部放入内存，并假定每个输入流都是已排序的（从小到大）。

具有两个可选参数，它们都必须指定为关键字参数。

key 指定带有单个参数的 key function，用于从每个输入元素中提取比较键。 默认值为 None (直接比较元素)。

reverse 为一个布尔值。 如果设为 True，则输入元素将按比较结果逆序进行合并。 要达成与 sorted(itertools.chain(*iterables), reverse=True) 类似的行为，所有可迭代对象必须是已从大到小排序的。

在 3.5 版更改: 添加了可选的 key 和 reverse 形参。

heapq.nlargest(n, iterable, key=None)
从 iterable 所定义的数据集中返回前 n 个最大元素组成的列表。 如果提供了 key 则其应指定一个单参数的函数，用于从 iterable 的每个元素中提取比较键 (例如 key=str.lower)。 等价于: sorted(iterable, key=key, reverse=True)[:n]。

heapq.nsmallest(n, iterable, key=None)
从 iterable 所定义的数据集中返回前 n 个最小元素组成的列表。 如果提供了 key 则其应指定一个单参数的函数，用于从 iterable 的每个元素中提取比较键 (例如 key=str.lower)。 等价于: sorted(iterable, key=key)[:n]。

后两个函数在 n 值较小时性能最好。 对于更大的值，使用 sorted() 函数会更有效率。 此外，当 n==1 时，使用内置的 min() 和 max() 函数会更有效率。 如果需要重复使用这些函数，请考虑将可迭代对象转为真正的堆。
"""

if __name__ == '__main__':
    a = [4,5,2,7,9]
    b = [3,6,7]
    heapq.heapify(a)
    print(a)
    heapq.heappush(a,10)
    print(a)
    heapq.heappop(a)
    print(a)
    heapq.heappushpop(a, 1)
    print(a)
    # heapq.heapreplace(a, 13)
    # print(a)
    heapq.heappushpop(a, 13)
    print(a)
    c = heapq.merge(a,b)
    for i in c:print(i)
    print(heapq.nlargest(2, a))
    print(heapq.nsmallest(2, a))
