# -*- coding:utf-8 -*-
"""
判断密码强度 break和continue语句，限制密码尝试次数
保存密码及强度到文件。读取保存文件
定义一个类，封装处理过程。
用类封装文件操作
20171219
v6.0
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

    # 判断密码是否同时包含大小写字母
    def check_up_and_low(self):
        is_up = False
        is_low = False
        for c in self.password:
            if c.isalpha():
                if c.isupper():
                    is_up = True
                else:
                    is_low = True
        if is_up == True and is_low == True:
            return True
        return False



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

        # 同时包含大小写
        if self.check_up_and_low():
            self.strength_level += 1
        else:
            print("密码必须同时包含大小写字母!")


class FileTool:
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, line):
        f = open(self.filepath, "a")
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath, "r")
        lines = f.readlines()
        f.close()
        return lines

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

    file_tool = FileTool("password_6.0.txt")
    while try_times > 0:

        password = input("请输入密码:")
        password_tool = PasswordTool(password)
        password_tool.process_password()

        # f = open("password_5.0.txt", "a")
        # f.write("密码:{},强度:{}\n".format(password, password_tool.strength_level))
        # f.close()

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


        line = "密码:{},强度:{}\n".format(password, password_tool.strength_level)
        file_tool.write_to_file(line)

        if password_tool.strength_level == 4:
            print("密码强度合格")
            break
        else:
            print("密码强度过低，请重新设定。")
            try_times -= 1
    if try_times <= 0:
        print("尝试次数过多，密码设置失败")
    else:
        print("密码设置成功")
    lines = file_tool.read_from_file()
    print(lines)

if __name__ == "__main__":
    main()