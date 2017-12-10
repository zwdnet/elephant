# -*- coding:utf-8 -*-
"""
绘制五角星，绘制不同大小的五角星
版本:3.0
日期:20171209
使用递归函数
"""
import turtle
import random


def draw_pantagram(size):
    count = 1
    color = ["black", "red", "green", "yellow", "blue"]
    c = random.randint(0, 4)
    turtle.pencolor(color[c])
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1


def draw_recursive_pentagram(size):
    """
    迭代绘制
    """
    count = 1
    color = ["black", "red", "green", "yellow", "blue"]
    c = random.randint(0, 4)
    turtle.pencolor(color[c])
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1
    size += 20
    if size <= 500:
        draw_recursive_pentagram(size)

def main():
    size = 50
    turtle.penup()
    turtle.bk(200)
    turtle.pendown()
    turtle.speed("fastest")

    draw_recursive_pentagram(size)
    turtle.exitonclick()


if __name__ == '__main__':
    main()