# -*- coding:utf-8 -*-
"""
BMR计算器
版本1.0
日期：20171211
"""


def main():
    # 性别
    gender = '女'
    # 体重
    weight = 70
    # 身高
    height = 175
    # 年龄
    age = 25
    if gender == '男':
        # 男性
        bmr = 13.7*weight + 5.0*height - 6.8*age + 66
    elif gender == '女':
        # 女性
        bmr = 9.6*weight + 1.8*height - 4.7*age + 655
    else:
        bmr = -1

    if bmr != -1:
        print("基础代谢率(大卡):", bmr)
    else:
        print("暂不支持该性别")

if __name__ == "__main__":
    main()