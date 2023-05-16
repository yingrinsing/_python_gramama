#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-10-20

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
import xlrd
import time
from xlwt import Workbook
from pyExcelerator import *
#===============================================================================
# 
#===============================================================================
# def _lktest():
#     obj = None
#     laok.dump_description_help(obj)
def read_excel(filename):
    # 打开文件
    #workbook = xlrd.open_workbook(r'F:\demo.xlsx')
    workbook = xlrd.open_workbook(filename)
    # 获取所有sheet
    print workbook.sheet_names() # [u'sheet1', u'sheet2']
    sheet1_name = workbook.sheet_names()[1]

    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始
    sheet1 = workbook.sheet_by_name('Sheet1')

    # sheet的名称，行数，列数
    print sheet1.name,sheet1.nrows,sheet1.ncols

    # 获取整行和整列的值（数组）
    rows = sheet1.row_values(0) # 获取第一行内容
    cols = sheet1.col_values(2) # 获取第三列内容
    cols_str = str(sheet1.row_values(2)).decode("unicode_escape").encode("utf8") 
    cols_str1 = str(sheet1.row_values(2)).encode("utf8")   
    print rows
    print cols
    print cols_str
    print cols_str1
    
    # 获取单元格内容
    print sheet1.cell(1,0).value.encode('utf-8')
    print sheet1.cell_value(1,0).encode('utf-8')
    print sheet1.row(1)[0].value.encode('utf-8')
    
    # 获取单元格内容的数据类型
    print sheet1.cell(1,0).ctype    
    
def read_excel1(filename, index = 0):
    # 打开文件
    workbook = xlrd.open_workbook(filename)
    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(index) # sheet索引从0开始
    return sheet1

def write_file():
    # excel 第一行数据
    excel_headDatas = [u'发布时间', u'文章标题', u'文章链接', u'文章简介']
    articles =[
        {u'发布时间':u'2017年5月9日',
         u'文章标题':u'Python项目实战教程：国内就能访问的google搜索引擎',
         u'文章链接':'http://mp.weixin.qq.com/s?timestamp=1494557315',
         u'文章简介':u'大家可以留言、想了解python那个方向的知识、不然我也不知道'},
    
        {u'发布时间':u'2017年5月4日',
         u'文章标题':u'对于学习Django的建议、你知道的有那些',
         u'文章链接':'http://mp.weixin.qq.com/s?timestamp=1494557323',
         u'文章简介':u'随着Django1.4第二个候选版的发布，虽然还不支持Python3，但Django团队已经在着手计划中，据官方博客所说，Django1.5将会试验性的支持python3'}
    ]
    # 定义excel操作句柄
    excle_Workbook = Workbook()
    excel_sheet_name = time.strftime('%Y-%m-%d')
    excel_sheet = excle_Workbook.add_sheet(excel_sheet_name)
    index = 0
    #标题
    for data in excel_headDatas:
        excel_sheet.write(0, index, data)
        index += 1
    
    index = 1
    
    #内容
    for article in articles:
        colIndex = 0
        for item in excel_headDatas:
            excel_sheet.write(index, colIndex, article[item])
            colIndex += 1
        index += 1
    #保存test.xlsx到当前程序目录
    excle_Workbook.save('test.xlsx')


if __name__ == '__main__':
    #read_excel('indicator.xlsx')#catch_except = True
    write_file()