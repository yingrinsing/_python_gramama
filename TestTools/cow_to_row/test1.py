# -*- coding: utf-8 -*-
# @Time    : 2020-04-30 16:42
# @Author  : yingrinsing
# @File    : test1.py

"""

功能说明

"""

import os
import re
from File import File

def findall_str(test_str ,str_patterm, str_type = 'en'):
    if str_type == 'ch':
        test_str = test_str.decode('UTF-8')
    new_str_list = re.findall(str_patterm, test_str)
    return new_str_list[0].encode('UTF-8')

def test():
    file_path = str(os.path.abspath(os.path.join(os.getcwd(), "."))) + '/test_cow.csv'
    # 读取数据库模板数据
    test_list = []
    data_list = File.read_csv_list(file_path)
    for data in data_list:
        test_list.append('"'+data+'"')
    print(','.join(test_list))



if __name__ == '__main__':
    test()