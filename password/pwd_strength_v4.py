# -*- coding:utf-8 -*-
"""
判断密码强度 break和continue语句，限制密码尝试次数
保存密码及强度到文件。读取保存文件
20171218
v4.0
"""


# 判断字符串中是否含有数字
def check_number_exist(password_str):
    has_number = False
    for c in password_str:
        if c.isnumeric():
            has_number = True
            break
    return has_number


def check_letter_exist(password_str):
    has_letter = False
    for c in password_str:
        if c.isalpha():
            has_letter = True
            break
    return has_letter


def main():
    try_times = 5

    while try_times > 0:

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

        # f = open("password_3.0.txt", "a")
        # f.write("密码:{},强度:{}\n".format(password, strength_level))
        # f.close()

        f = open("password_3.0.txt", "r")
        # content = f.read()
        # print(content)
        line = f.readline()
        print(line)
        line = f.readline()
        print(line)

        lines = f.readlines()
        print(lines)
        for line in f:
            print(line)
        f.close()

        if strength_level == 3:
            print("密码强度合格")
            break
        else:
            print("密码强度过低，请重新设定。")
            try_times -= 1
    if try_times <= 0:
        print("尝试次数过多，密码设置失败")
    else:
        print("密码设置成功")

if __name__ == "__main__":
    main()