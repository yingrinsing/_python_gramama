# -*- coding: utf-8 -*-
# @Time    : 2019-12-02 13:02
# @Author  : yingrinsing
# @File    : test.py

"""

功能说明

"""
# !/usr/bin/python
# coding=utf8

import os, sys

# 工资税率
month_tax = [[0, 3, 0], [36000, 10, 2520], [144000, 20, 16920], [300000, 25, 31920], [420000, 30, 52920],
             [660000, 35, 85920], [960000, 45, 181920]]

# 年终奖税率
year_tax = [[0, 3, 0], [3000, 10, 210], [12000, 20, 1410], [25000, 25, 2660], [35000, 30, 4410], [55000, 35, 7160],
            [80000, 45, 15160]]

# 起征点
threshold_of_personal_income_tax = 5000

# 社保缴费上限
max_social_security_base = 25401

# 公积金缴费基数上限
max_housing_fund_base = 27786


# 根据薪水获取社保扣除
def social_security_remission(salary):
    # 公积金
    remission = min(salary, max_housing_fund_base) * 12.0 / 100
    # 其他
    remission += min(salary, max_social_security_base) * 10.2 / 100

    return remission


# 年度税后月薪总额计算
# remission 减免项，包括租房、子女教育、父母赡养等
# bonus_factor  1月奖金月数，包括年度加班费等
# salary_incr_factor 4月调薪比例
def month_salary_after_tax(salary, remission, bonus_factor, salary_incr_factor):
    sum_for_tax = 0  # 计税总额
    sum_salary_after_tax = 0  # 税后年度收益
    tax_level = 0  # 计税区间
    all_tax = 0  # 年度纳税总额

    for i in range(1, 13):
        if i >= 4: salary += salary * salary_incr_factor  # 调薪

        insurance_remission = social_security_remission(salary)  # 社保减免

        tax_input = salary - remission - insurance_remission - threshold_of_personal_income_tax  # 计税额度
        if i == 1: tax_input += salary * bonus_factor  # 奖金
        sum_for_tax += tax_input

        tax = 0
        if sum_for_tax > 0:
            if tax_level < len(month_tax) - 1 and sum_for_tax > month_tax[tax_level + 1][0]:
                tax_level += 1
            tax = sum_for_tax * month_tax[tax_level][1] / 100 - month_tax[tax_level][2] - all_tax
            all_tax += tax

        salary_after_tax = tax_input - tax + threshold_of_personal_income_tax + remission
        # print "month-%d  %d" %(i,salary_after_tax)
        sum_salary_after_tax += salary_after_tax
    return sum_salary_after_tax


# 年终奖计算
def year_end_bonus_after_tax(salary, bonus_factor):
    salary_before_tax = salary * bonus_factor
    per_month = salary_before_tax / 12.

    tax_level = 0
    for i in range(0, len(year_tax)):
        if per_month > year_tax[i][0]:
            tax_level = i
    tax = salary_before_tax * year_tax[tax_level][1] / 100 - year_tax[tax_level][2]
    return salary_before_tax - tax


if __name__ == "__main__":
    argv = sys.argv

    if len(argv) != 6:
        print("Usage:%s     " % (argv[0]))
        print("\tsalary:月薪")
        print("\tremission:每月减免额度，如租房、子女教育等")
        print("\tovertime-pay-factor:每年加班费折算月数")
        print("\tsalary-incr-factor:4月调薪增幅")
        print("\tyear-end-bonus-factor:年终奖月数")
        sys.exit(0)

    salary = float(argv[1])
    remission = float(argv[2])
    overtime_pay_factor = float(argv[3])
    salary_incr_factor = float(argv[4])
    year_end_bonus_factor = float(argv[5])

    split = month_salary_after_tax(salary, remission, overtime_pay_factor + 2,
                                   salary_incr_factor) + year_end_bonus_after_tax(salary, year_end_bonus_factor - 2)
    merge = month_salary_after_tax(salary, remission, overtime_pay_factor,
                                   salary_incr_factor) + year_end_bonus_after_tax(salary, year_end_bonus_factor)

    print("分开发放：%d" % (split))
    print("合并发放：%d" % (merge))
    print("合并发放 - 分开发放：%d" % (merge - split))