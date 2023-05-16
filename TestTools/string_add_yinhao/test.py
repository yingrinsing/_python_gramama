# -*- coding: utf-8 -*-
# @Time    : 2021/12/31 下午3:22
# @Author  : yingrinsing
# @File    : test.py

"""

功能说明

"""

str = "guying,likaisong,shiruolin,wb_daiquanguang,wb_liangyu03,wb_lijilong,wb_liuhuaqing,wb_liulu07,wb_liunana,wb_maozhenghui,wb_nieshuxian,wb_panshanshan,wb_tangfujie,wb_tangping,wb_tengtingting,wb_wangtianfeng,wb_wangxiaoyang,wb_xiangyang03,wb_xucuilin,wb_zhulintao,xieyifan03,yexiali,yinjian,yuyi05,zhaofan03"

temp_list = str.split(",")

new_temp_list = ['\"'+s+'\"' for s in temp_list]
new_str = ",".join(new_temp_list)
print(new_str)