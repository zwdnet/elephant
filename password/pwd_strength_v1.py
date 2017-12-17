# -*- coding:utf-8 -*-
"""
判断密码强度
20171217
v1.0
"""


# 判断字符串中是否含有数字
def check_number_exist(password_str):
    for c in password_str:
        if c.isnumeric():
            return True
    return False


def check_letter_exist(password_str):
    for c in password_str:
        if c.isalpha():
            return True
    return False


def main():
    password = input("请输入密码:")
    # 密码强度变量
    strength_level = 0

    # 规则一 密码长度大于8
    if len(password) >= 8:
        strength_level += 1
    else:
        print("密码长度至少8位")

    # 包涵数字
    if check_number_exist(password):
        strength_level += 1
    else:
        print("密码要求包含数字！")

    # 包涵字母
    if check_letter_exist(password):
        strength_level += 1
    else:
        print("密码要求包含字母！")

    if strength_level == 3:
        print("密码强度合格")
    else:
        print("密码强度过低，请重新设定。")

if __name__ == "__main__":
    main()