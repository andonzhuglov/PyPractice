from turtle import Turtle, Screen
from random import randint, choice
arrow = Turtle()
screen = Screen()
arrow.width(15)
arrow.ht()
screen.bgcolor("black")
arrow.speed("fastest")

colors = ["NavajoWhite", "GreenYellow", "SkyBlue", "Orchid", "BlueViolet", "Aquamarine"]
directions = [0, 90, 180, 270]

for x in range(200):
    arrow.color(choice(colors))
    arrow.forward(30)
    arrow.setheading(choice(directions))