#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""
# import pandas as pd
# =========================================================================
# 
# ===============================================================================
import pandas


def read_excel_file(filename,sheetname):
    df = pandas.read_excel(filename, sheet_name=sheetname)
    print(df)
    # 打印头部数据
    print(df.head())
    # 打印列标题
    print(df.columns)
    # 打印行
    print(df.index)
    print(df["7点"])


if __name__ == '__main__':
    filename = "6月龄宝宝辅食表.xlsx"
    read_excel_file(filename,"6")

