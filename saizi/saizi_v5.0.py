# -*- coding:utf-8 -*-
"""
功能：模拟掷2个骰子。科学计算
版本：5.0
日期：20171222
"""

import numpy as np
import matplotlib.pyplot as plt

def roll_dice():
    roll = np.random.randint(1,6)
    return roll


def main():
    total_times = int(input("输入模拟次数:"))

    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    roll3_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr + roll3_arr

    hist, bins = np.histogram(result_arr, bins = range(2, 20))
    print(hist)
    print(bins)

    tick_labels = ['2点', '3点', '4点', '5点', '6点',
                    '7点', '8点', '9点', '10点', '11点', '12点', '13点',
                    '14点', '15点', '16点', '17点', '18点']
    tick_pos = np.arange(2, 19) + 0.5
    plt.xticks(tick_pos, tick_labels)
    plt.hist(result_arr, bins = range(2, 20), normed = 1, edgecolor = 'black', linewidth = 1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("点数统计图")
    plt.show()

if __name__ == "__main__":
    main()