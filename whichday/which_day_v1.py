# -*- coding:utf-8 -*-
"""
版本 1.0
日期：20171216
功能：输入日期，判断是某年的第几天
"""
from datetime import datetime


def main():
    input_date_str = input("请输入日期(yyyy/mm/dd):")
    input_date = datetime.strptime(input_date_str, "%Y/%m/%d")
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 计算天数，不包含闰年的情况
    days_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = sum(days_in_month_tup[:month-1]) + day

    # 处理闰年情况
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0) ):
        if month > 2:
            days += 1

    print("这是第{}天".format(days))


if __name__ == "__main__":
    main()