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
import xlrd,xlwt


def read_handle_excel(filename,sheet_name):
    # 读Excel文件的数据
    data = xlrd.open_workbook(filename, formatting_info=True)
    # 获取第一个sheet
    table1 = data.sheet_by_index(0)
    # 获取指定的sheet
    table2 = data.sheet_by_name(sheet_name)
    dataList = []

    # 获取表总行数
    nrows = table1.nrows
    print("表格总行数%d" % nrows)
    ncols = table1.ncols
    print("表格总列数%d" % ncols)

    for rows in range(0,nrows):
        tempList = []
        for cols in range(0, ncols):
            tempList.append(table2.cell_value(rows,cols))
        print(tempList)
        dataList.append(tempList)
    print(dataList)
    return dataList


def write_excel(filename, sheet_name, data_list):
    if data_list:
        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet(sheet_name)
        nrows = len(data_list)
        ncols = len(data_list[0])
        for i in range(nrows):
            for j in range(ncols):
                ws.write(i,j,data_list[i][j])
        wb.save(filename)


if __name__ == '__main__':
    filename = "6月龄宝宝辅食表.xls"
    new_file = "6月宝宝.xls"
    data_list = read_handle_excel(filename,"6")
    write_excel(new_file, "6月", data_list)