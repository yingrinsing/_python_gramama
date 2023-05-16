# -*- coding: utf-8 -*-
# @Time    : 2019-10-10 20:27
# @Author  : yingrinsing
# @File    : xmind_to_excel.py

"""

功能说明

"""
import xml.etree.ElementTree as ET
import xlwt
import argparse

g_row = 0


def do_write_excel(text, row, col):
    # print text + " row %d + col %d"%(row, col)
    ws.write(row, col, text)


def perf_func(elem, func, level = 0):
    global g_row
    func(elem, g_row, level)

    for child in list(elem):
        name = child.get('TEXT')

        perf_func(child, func, level + 1)
        if child.find('node') is None and name is not None:
            g_row = g_row + 1


def write_excel(elem, row, level):
    name = elem.get('TEXT')
    if name is not None:
        do_write_excel(name, row, level)


parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input-file', type=str, dest='inputfile', required=True)
parser.add_argument('-o', '--output-file', type=str, dest='outputfile', default='freemind2excel.xls', help='Default outputfile is freemind2excel.xls')
args = parser.parse_args()

if args.inputfile is None:
    parser.print_help()
    exit()

root = ET.parse(args.inputfile)
map_version = root.getroot()
first_node = map_version.find('node')

wb = xlwt.Workbook()
ws = wb.add_sheet('freemind2excel')

perf_func(first_node, write_excel)

wb.save(args.outputfile)