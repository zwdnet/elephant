# -*- coding:utf-8 -*-
"""
功能：模拟掷骰子
版本：1.0
日期：20171220
"""

import random

def roll_dice():
    roll = random.randint(1,6)
    return roll


def main():
    total_times = int(input("输入模拟次数:"))
    result_list = [0]*6

    for i in range(total_times):
        roll = roll_dice()
        result_list[roll-1] += 1

    for i,result in enumerate(result_list):
        print("点数{}的次数{},频率{}".format(i+1, result, result/total_times))

if __name__ == "__main__":
    main()