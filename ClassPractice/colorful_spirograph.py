import turtle
from turtle import Turtle, Screen
from random import randint
arrow = Turtle()
screen = Screen()
screen.bgcolor("black")
turtle.colormode(255)
arrow.width(1)
arrow.speed("fastest")


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(gap):
    for x in range(int(360 / gap)):
        arrow.color(random_color())
        arrow.circle(100)
        arrow.setheading(arrow.heading() + gap)

draw_spirograph(5)
screen.exitonclick()