# -*- coding:utf-8 -*-
"""
判断密码强度 break和continue语句，限制密码尝试次数
保存密码及强度到文件。读取保存文件
定义一个类，封装处理过程。
20171219
v5.0
"""


class PasswordTool:
    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    def check_number_exist(self):
        has_letter = False
        for c in self.password:
            if c.isnumeric():
                has_letter = True
                break
        return has_letter

    def check_letter_exist(self):
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter

    def process_password(self):
        # 规则一 密码长度大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print("密码长度至少8位")

        # 包涵数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print("密码要求包含数字！")

        # 包涵字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print("密码要求包含字母！")


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
        password_tool = PasswordTool(password)
        password_tool.process_password()

        f = open("password_5.0.txt", "a")
        f.write("密码:{},强度:{}\n".format(password, password_tool.strength_level))
        f.close()

        # f = open("password_3.0.txt", "r")
        # content = f.read()
        # print(content)
        # line = f.readline()
        # print(line)
        # line = f.readline()
        # print(line)
        #
        # lines = f.readlines()
        # print(lines)
        # for line in f:
        #     print(line)
        # f.close()

        if password_tool.strength_level == 3:
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