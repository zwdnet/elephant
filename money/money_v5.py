# -*- coding:utf-8 -*-
"""
52周存钱挑战
日期：20171215
版本 5.0
根据用户输入的日期，判断是一年中的第几周，然后输出相应的存款金额。
"""
import math
import datetime

saving = 0


# 计算n周内的存款金额
def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    global saving
    saving = 0            # 存的钱数

    money_list = []       # 记录每周存款数列表
    saved_money_list = [] # 记录每周账户累计

    # while i <= total_week:
    for i in range(total_week):
        # saving += money_per_week
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)

        # 输出信息
        print("第{}周，存入{}元，账户累计{}元".format(i+1, money_per_week, saving))
        money_per_week += increase_money
        # i += 1
    # print("函数内saving:", saving)
    return saved_money_list


def main():
    money_per_week = float(input("请输入每周存入金额:"))  # 每周存入金额
    increase_money = float(input("请输入每周递增金额:"))   # 每周递增金额
    total_week = int(input("请输入存款周数"))       # 存钱周数
    saved_money_list = save_money_in_n_weeks(money_per_week, increase_money, total_week)
    input_data_str = input("请输入日期(yyyy/mm/dd):")
    input_data = datetime.datetime.strptime(input_data_str, "%Y/%m/%d")
    week_num = input_data.isocalendar()[1]
    # week_num = int(input("请输入第几周:"))
    print("第{}周存款{}元".format(week_num, saved_money_list[week_num - 1]))

if __name__ == "__main__":
    main()