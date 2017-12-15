# -*- coding:utf-8 -*-
"""
版本 3.0
日期：20171217
功能：输入日期，判断是某年的第几天 用集合代替列表
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

    _30_days_month_set = {4, 6, 9, 11}
    _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}

    days = 0
    days += day
    for i in range(1, month):
        if i in _30_days_month_set:
            days += 30
        elif i in _31_days_month_set:
            days += 31
        else: # 2月份
            days += 28

    # 处理闰年情况
    if is_leap_year(year) == True and month > 2:
        days += 1

    print("这是{}年的第{}天".format(year, days))


if __name__ == "__main__":
    main()