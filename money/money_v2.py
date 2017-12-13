# -*- coding:utf-8 -*-
"""
52周存钱挑战
日期：20171213
版本 2.0
记录每周存款数
"""
import math


def main():
    money_per_week = 10   # 每周存入金额
    i = 1                 # 周数
    increase_money = 10   # 每周递增金额
    total_week = 52       # 存钱周数
    saving = 0            # 存的钱数

    money_list = []       # 记录每周存款数列表

    while i <= total_week:
        # saving += money_per_week
        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # 输出信息
        print("第{}周，存入{}元，账户累计{}元".format(i, money_per_week, saving))
        money_per_week += increase_money
        i += 1


if __name__ == "__main__":
    main()