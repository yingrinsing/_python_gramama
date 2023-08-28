# -*- coding: utf-8 -*-
# @Time    : 2019-08-01 14:25
# @Author  : yingrinsing
# @File    : RandomData.py

"""

1、获取随机数据、
2、获取当前特定格式的时间戳
3、获取MD5加密字符串
4、获取sign字段的加密算法
"""


import random
import string
import hashlib
import datetime
import time
import re
from xeger import Xeger
import uuid

def choice_data(data):
    """
    获取随机整型数据
    :param data: 数组
    :return:
    """
    _list = data.split(",")
    num = random.choice(_list)
    return num


def random_float(data):
    """
    获取随机整型数据
    :param data: 数组
    :return:
    """
    try:
        start_num, end_num, accuracy = data.split(",")
        start_num = int(start_num)
        end_num = int(end_num)
        accuracy = int(accuracy)
    except ValueError:
        raise Exception("调用随机整数失败，范围参数或精度有误！\n小数范围精度 %s" % data)

    if start_num <= end_num:
        num = random.uniform(start_num, end_num)
    else:
        num = random.uniform(end_num,start_num)
    num = round(num, accuracy)
    return num


def md5(data):
    """
    md5加密
    :param data:想要加密的字符
    :return:
    """
    m1 = hashlib.md5()
    m1.update(data.encode("utf-8"))
    data = m1.hexdigest()
    return data


def random_int(scope):
    """
    获取随机整型数据
    :param scope: 数据范围
    :return:
    """
    try:
        start_num, end_num = scope.split(",")
        start_num = int(start_num)
        end_num = int(end_num)
    except ValueError:
        raise Exception("调用随机整数失败，范围参数有误！\n %s" % str(scope))
    if start_num <= end_num:
        num = random.randint(start_num, end_num)
    else:
        num = random.randint(end_num, start_num)

    return num


def random_string(num_len, str_type='all'):
    """
    默认从a-zA-Z0-9生成制定数量的随机字符
    :param num_len: 字符串长度
    :param str_type: 字符串长度,all：a-zA-Z0-9 number:0-9
    :return:
    """
    try:
        num_len = int(num_len)
    except ValueError:
        raise Exception("从a-zA-Z0-9生成指定数量的随机字符失败！长度参数有误  %s" % num_len)
    if str_type == 'number':

        strings = ''.join([str(random_int('0,9')) for i in range(+num_len)])
    else:
        strings = ''.join(random.sample(string.hexdigits, +num_len))
    return strings


def random_boundary():
    """
    随机生成上传符
    :return:
    """
    return str(random.randint(1e28, 1e29 - 1))


def get_time(time_type, layout, unit="0,0,0,0,0"):
    """
    获取时间
    :param time_type: 现在的时间now， 其他时间else_time
    :param layout: 10timestamp，13timestamp, else  时间类型
    :param unit: 时间单位：[seconds, minutes, hours, days, weeks] 秒，分，时，天，周，所有参数都是可选的，并且默认都是0
    :return:
    """
    ti = datetime.datetime.now()
    if time_type != "now":
        resolution = unit.split(",")
        try:
            ti = ti + datetime.timedelta(seconds=int(resolution[0]), minutes=int(resolution[1]),
                                         hours=int(resolution[2]), days=int(resolution[3]), weeks=int(resolution[4]))
        except ValueError:
            raise Exception("获取时间错误，时间单位%s" % unit)
    if layout == "10timestamp":
        ti = ti.strftime('%Y-%m-%d %H:%M:%S')
        ti = int(time.mktime(time.strptime(ti, "%Y-%m-%d %H:%M:%S")))
        return ti
    elif layout == "13timestamp":
        ti = ti.strftime('%Y-%m-%d %H:%M:%S')
        ti = int(time.mktime(time.strptime(ti, '%Y-%m-%d %H:%M:%S')))
        # round()是四舍五入
        ti = int(round(ti * 1000))
        return ti
    else:
        ti = ti.strftime(layout)
        return ti


def random_pattern(pattern):
    """
    根据正则表达式随机生成字符串
    :param pattern: api路径?后面的参数格式
    :return:
    """
    _x = Xeger()
    test_str = _x.xeger(pattern)
    return test_str


def get_upper_uuid():
    """
        生成大写的uuid
        :return:
        """
    return str(uuid.uuid4()).upper()


def get_xf_sign(params_data, form_data):
    """
    笑番获取签名
    :param params_data: api路径?后面的参数格式
    :param form_data: form格式的传参数据
    :return:
    """
    new_dict = {}
    if params_data:
        new_dict.update(params_data)
    if form_data:
        new_dict.update(form_data)
    sort_new_dict_list = sorted(new_dict.items(), key=lambda x: x[0])
    new_list = []
    for dl in sort_new_dict_list:
        new_list.append(str(dl[0]) + '=' + str(dl[1]))
    final_str = '&'.join(new_list)
    final_str += "&accessSecret=3refdgdEDCRTGFDVASDCZX456yhs"
    sign_str = md5(final_str).upper()
    return sign_str


def get_ky_sign(params_data, form_data):
    """
    快影获取sing签名
    :param params_data: api路径?后面的参数格式
    :param form_data: form格式的传参数据
    :return:
    """
    new_dict = {}
    if params_data:
        new_dict.update(params_data)
    if form_data:
        new_dict.update(form_data)
    sort_new_dict_list = sorted(new_dict.items(), key=lambda x: x[0])
    new_list = []
    for dl in sort_new_dict_list:
        new_list.append(str(dl[0]) + '=' + str(dl[1]))
    final_str = '&'.join(new_list)
    final_str += "&accessSecret=3refdgdEDCRTGFDSFASDFASoiwqeurcvVASDCZX456yhs"
    sign_str = md5(final_str).upper()
    return sign_str


def get_h5_sign(nonce, timestamp, key='3edctyueiwochnyedjxvbxjzkisjchgdnx38uejd'):
    """
    :param nonce: 为12位随机数
    :param timestamp: 13位timestamp(时间戳)参数
    :param key: app特殊标签，edctyueiwochnyedjxvbxjzkisjchgdnx38uejd为笑番对应的key
    :return:
    """
    # 笑番key = '3edctyueiwochnyedjxvbxjzkisjchgdnx38uejd'
    # 年汤圆key = 'YHNFG567FG7898yihkj67ryhjFVHBJ6yug98yihkj'

    uni_hex_str = ''.join([hex(ord(i)).replace("0x", "") for i in key])
    uni_hex_str_new = re.sub('[a-f]', '', uni_hex_str)[0:16]
    tmp = int(uni_hex_str_new)
    handle_str = str(int(nonce) ^ (tmp ^ int(timestamp) | tmp))
    sign = md5(handle_str)
    return sign


if __name__ == "__main__":
    # test = random_pattern('^[\u4E00-\u9FA5A-Za-z0-9_]{4,10}$')
    # print(test)
    nonce = random_string(12,'number')
    print(nonce)
    timestamp = get_time("now", "13timestamp")
    print(timestamp)
    # print(get_h5_sign(nonce, timestamp))
    t = int(nonce)
    print(get_h5_sign(nonce,timestamp))