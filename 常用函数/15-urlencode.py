# -*- coding: utf-8 -*-
# @Time    : 2023/6/15 3:21 下午
# @Author  : yingrinsing
# @File    : 15-urlencode.py

"""

功能说明

"""
from urllib.parse import urlencode, quote_plus

basic_video_check = {"dynamicParams":{"d":"true"}}

dynamic_params = urlencode(basic_video_check, quote_via=quote_plus)
print(dynamic_params)