# -*- coding:utf-8 -*-
"""
版本 4.0
日期：20171217
功能：输入日期，判断是某年的第几天 用字典
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

    # _30_days_month_set = {4, 6, 9, 11}
    # _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}

    month_day_dict = {1:31,
                      2:28,
                      3:31,
                      4:30,
                      5:31,
                      6:30,
                      7:31,
                      8:31,
                      9:30,
                      10:31,
                      11:30,
                      12:31}
    day_month_dict = {30:{4, 6, 9, 11},
                      31:{1, 3, 5, 7, 8, 10, 12}}

    days = 0
    days += day
    for i in range(1, month):
        days += month_day_dict[i]
    # 处理闰年情况
    if is_leap_year(year) == True and month > 2:
        days += 1

    print("方法一")
    print("这是{}年的第{}天".format(year, days))

    days = day
    for i in range(1, month):
        if i in day_month_dict[30]:
            days += 30
        elif i in day_month_dict[31]:
            days += 31
        else: # 2月
            days += 28

    # 处理闰年情况
    if is_leap_year(year) == True and month > 2:
        days += 1

    print("方法二")
    print("这是{}年的第{}天".format(year, days))

    # 方法3,用库
    print("方法三")
    print("这是{}年的第{}天".format(year, input_date.strftime('%j')))


if __name__ == "__main__":
    main()