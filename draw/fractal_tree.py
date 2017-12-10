# -*- coding:utf-8 -*-
"""
绘制分形树
版本:1.0
日期:20171210
使用递归函数
"""
import turtle


def chooseColor(length):
    if length < 5:
            turtle.color('green')
    else:
            turtle.color('black')

# 画分形树
def draw_branch(branch_length):
    short_length = 8
    if branch_length > 5:
        chooseColor(branch_length - short_length)
        # 绘制右侧树枝
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length - short_length)

        # 绘制左侧树枝
        turtle.left(40)
        draw_branch(branch_length - short_length)

        # 返回之前树枝
        turtle.penup()
        turtle.right(20)
        turtle.backward(branch_length)
        turtle.pendown()


def main():
    turtle.left(90)
    turtle.speed("fastest")
    turtle.penup()
    turtle.backward(300)
    turtle.pendown()
    draw_branch(100)
    turtle.exitonclick()


if __name__ == '__main__':
    main()