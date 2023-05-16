# -*- coding: utf-8 -*-
# @Time    : 2019-09-09 15:52
# @Author  : yingrinsing
# @File    : File.py

"""

功能说明  读写excel或者csv文件

"""
from codecs import open
import csv
import os

class File:
    def __init__(self):
        self._cache_file = {}

    @staticmethod
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

    @staticmethod
    def write_csv(filename, iter_data):
        """
            写入csv 格式的文件
            :filename:输入写文件的路径
            :iter_data:输入可迭代的字典
            :return:
        """
        fmt_line = None
        with open(filename=filename, mode='w', encoding='utf8') as f:
            for data in iter_data:
                if not fmt_line:
                    fmt_line = u",".join(u"{%s}" % k for k in data) + u'\n'
                    f.write(fmt_line.replace('{', '').replace('}', ''))
                #             print(fmt_line.format(**data))
                f.write(fmt_line.format(**data))

    @staticmethod
    def read_csv_list(filename):
        """
            读取csv 格式的单列表文件
            :filename:输入读文件的路径
            :return:
        """
        csv_list = []
        with open(filename=filename, mode='r', encoding='utf-8-sig') as csvfile:
            # spam_reader = csv.reader(csvfile)
            for row in csvfile.readlines():
                csv_list.append(row.strip())
            return csv_list

    @staticmethod
    def write_csv_list(filename, iter_data):
        """
            读取csv 格式的单列表文件
            :filename:输入读文件的路径
            :return:
        """
        with open(filename=filename, mode='a', encoding='utf-8') as f:
            for data in iter_data:
                data = data + '\n'
                f.write(data)

    @staticmethod
    def save_file(url, dlfolder):
        '''
        把下载后的文件保存到下载目录
        :param url: 真实的下载链接
        :param dlfolder: 下载目录
        :return: None
        '''
        # 获取跳转后的真实下载链接
        # req = urllib.request.Request(url)
        # req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')
        # response = urllib.request.urlopen(req)
        # dl_url = response.geturl()  # 跳转后的真实下载链接

        os.chdir(dlfolder)  # 跳转到下载目录

        # 从真实的下载链接下载文件
        dl_req = urllib.request.Request(url)
        dl_req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')
        dl_response = urllib.request.urlopen(dl_req)
        dl_file = dl_response.read()

        filename = url.split('?')[0].split('/')[-1]  # 获取下载文件名
        with open(filename, 'wb') as f:
            f.write(dl_file)
            f.close()

    # 写文件
    def write_file(self, filename, msg):
        if filename not in self._cache_file:
            self._cache_file[filename] = open(filename, mode='a', encoding='utf-8')
        # print(filename)
        # _cache_file[filename].write(codecs.BOM_UTF8)
        self._cache_file[filename].write("%s\n" % msg)
        self._cache_file[filename].flush()