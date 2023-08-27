#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""
import csv
import os


# =========================================================================
# 
# ===============================================================================
def read_file_basic(filename):
    with open(filename, mode="r", encoding="utf8") as f:
        names = f.readline().strip("\n").split(",")
        for line in f:
            lines = line.strip("\n").split(",")
            assert len(names) == len(lines), line
            res_dict = {names[i]: lines[i] for i in range(len(lines))}
            yield res_dict


def write_file_basic(filename, iterdata):
    fmt_line = None
    with open(filename, mode="w", encoding="utf8") as f:
        for data in iterdata:
            if not fmt_line:
                fmt_line = ",".join("{%s}" % k for k in data)
                f.write(fmt_line.replace("{", "").replace("}", ""))
            f.write(fmt_line.format(**data))


def read_file_csv_list(filename):
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            yield row


def write_file_csv_list(read_file, write_file):
    iterdata = read_file_csv_list(read_file)
    with open(write_file, mode="w", newline="", encoding="utf-8-sig") as f:
        csv_writer = csv.writer(f)
        for data in iterdata:
            csv_writer.writerow(data)


def read_file_csv_dict(filename):
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def write_file_csv_dict(read_file, write_file):
    iterdata = read_file_csv_dict(read_file)
    fieldnames = ["字段物理名", "字段中文名"]
    with open(write_file, mode="w", newline="", encoding="utf-8-sig") as f:
        csv_writer = csv.DictWriter(f, fieldnames, extrasaction="ignore")
        csv_writer.writeheader()
        for data in iterdata:
            change_data = {field: data[field]+"he" for field in fieldnames}
            # for field in fieldnames:
            #     change_data[field] = data[field]+"你好"
            csv_writer.writerow(change_data)


if __name__ == '__main__':
    filename = "指标表元数据信息.csv"
    read_file_csv_list(filename)
    read_file_csv_dict(filename)
    write_file_csv_list(filename, "csv列表写表.csv")
    write_file_csv_dict(filename, "csv字典写表.csv")