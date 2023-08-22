# -*- coding: utf-8 -*-
# @Time    : 2021-02-03 21:51
# @Author  : yingrinsing
# @File    : resolution_test.py

"""

功能说明

"""
from codecs import open
import csv
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def read_csv(filename, delimiter=';'):
    """
        读取csv 格式的文件
        :filename:输入读文件的路径
        :return:
    """
    names = []
    with open(filename=filename, mode='r', encoding='utf-8-sig') as csvfile:
        spam_reader = csv.reader(csvfile, delimiter=delimiter, quotechar='"')
        for row in spam_reader:
            if not names:
                names = row
            else:
                assert len(names) == len(row), row
                val_dict = {
                    name if '.' not in name else name.replace('.', '_'): row[i]
                    for i, name in enumerate(names)
                }
                yield val_dict


def write_csv(filename, iter_data):
    u"""写入csv 格式的文件
    filename:输入写文件的路径
    iter_data:输入可迭代的字典
    """
    fmt_line = None
    with open(filename=filename, mode='w', encoding='utf8') as f:
        for data in iter_data:
            if not fmt_line:
                fmt_line = u",".join(u"{%s}" % k for k in data) + u'\n'
                f.write(fmt_line.replace('{', '').replace('}', ''))
            #             print(fmt_line.format(**data))
            f.write(fmt_line.format(**data))


def read_csv_lktest():
    iter_data = read_csv(u"指标表元数据信息.csv")
    for i, data in enumerate(iter_data):
        print i, u" ".join(u"%s:%s" % item for item in data.iteritems())


def write_csv_lktest():
    iter_data = read_csv(u"指标表元数据信息.csv")
    write_csv(u"指标表元数据信息-write.csv", iter_data)


# 写文件

_cache_file = {}


def write_file(filename, msg):
    if filename not in _cache_file:
        _cache_file[filename] = open(filename, mode='a', encoding='utf-8')
    # print(filename)
    # _cache_file[filename].write(codecs.BOM_UTF8)
    _cache_file[filename].write("%s\n" % msg)
    _cache_file[filename].flush()




if __name__ == '__main__':

    iter_resolution = read_csv('导入分辨率.csv',',')
    fmt_line = False
    filename = 'result.csv'
    header = 'width,height,is_resolution_new,is_resolution_old,result,malv_new,malv_old,result1\n'
    with open(filename=filename, mode='w', encoding='utf8') as f:
        for data in iter_resolution:
            if not fmt_line:
                f.write(header)
                fmt_line = True
            new_data=[]
            width = int(data['width'])
            height =int(data['height'])
            resolution_new,malv_new = is_resolution(width, height)
            resolution_old,malv_old = is_resolution_old(width, height)
            result = 'same' if resolution_new == resolution_old else 'different'
            new_data.append(str(width))
            new_data.append(str(height))
            new_data.append(resolution_new)
            new_data.append(resolution_old)
            new_data.append(result)
            new_data.append(str(malv_new))
            new_data.append(str(malv_old))
            new_data.append('yes' if malv_new < malv_old else 'no')
            f.write(','.join(new_data)+"\n")



    # print(a*b)
    # print(getNearLeast720P())
    # print(getNearLeast1080P())
    # print(getNearLeast4k())

