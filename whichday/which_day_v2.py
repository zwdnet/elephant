# -*- coding:utf-8 -*-
"""
版本 2.0
日期：20171216
功能：输入日期，判断是某年的第几天 用列表替换元组
"""
from datetime import datetime


def is_leap_year(year):
    """
    判断是否为闰年
    """
    is_leap = False
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0) ):
        is_leap = True
    return is_leap


def main():
    input_date_str = input("请输入日期(yyyy/mm/dd):")
    input_date = datetime.strptime(input_date_str, "%Y/%m/%d")

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 计算天数，不包含闰年的情况
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year) == True:
        days_in_month_list[1] = 29
    days = sum(days_in_month_list[:month-1]) + day
    #
    # # 处理闰年情况
    # if is_leap_year(year) == True and month > 2:
    #     days += 1

    print("这是{}年的第{}天".format(year, days))


if __name__ == "__main__":
    main()