# -*- coding:utf-8 -*-
"""
52周存钱挑战
日期：20171214
版本 4.0
灵活设置每周的存款数
"""
import math

saving = 0


# 计算n周内的存款金额
def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    global saving
    saving = 0            # 存的钱数

    money_list = []       # 记录每周存款数列表

    # while i <= total_week:
    for i in range(total_week):
        # saving += money_per_week
        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # 输出信息
        print("第{}周，存入{}元，账户累计{}元".format(i+1, money_per_week, saving))
        money_per_week += increase_money
        # i += 1
    print("函数内saving:", saving)


def main():
    money_per_week = float(input("请输入每周存入金额:"))  # 每周存入金额
    increase_money = float(input("请输入每周递增金额:"))   # 每周递增金额
    total_week = int(input("请输入存款周数"))       # 存钱周数
    save_money_in_n_weeks(money_per_week, increase_money, total_week)
    print("函数外saving:", saving)

if __name__ == "__main__":
    main()