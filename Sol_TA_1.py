import turtle
import random

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
colors=["red","green","black","blue","yellow","grey","cyan","orange"]

def draw_thing(l,c):
    for value in l:
        turtle.forward(value)
        turtle.pencolor(random.choice(c))
        turtle.stamp()
        turtle.backward(value)
        turtle.right(30)

draw_thing(list1,colors)
