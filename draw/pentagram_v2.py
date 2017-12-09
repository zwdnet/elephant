# -*- coding:utf-8 -*-
"""
绘制五角星，绘制不同大小的五角星
版本:2.0
日期:20171209
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

def main():
    size = 50
    turtle.penup()
    turtle.bk(200)
    turtle.pendown()
    turtle.speed("fastest")
    while size <= 500:
        draw_pantagram(size)
        size += 20
    turtle.exitonclick()


if __name__ == '__main__':
    main()