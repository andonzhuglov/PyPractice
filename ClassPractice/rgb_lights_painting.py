import turtle as turtle_model
from random import choice
arrow = turtle_model.Turtle()
screen = turtle_model.Screen()
turtle_model.colormode(255) # We need to state this each time we are going to use RGB for Colors.
# Color list generated with Colorgram from the code above:
color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48)]

arrow.speed("fastest")
arrow.ht()
arrow.penup()

arrow.setheading(225)
arrow.forward(300)
arrow.setheading(0)

for dots in range(1, 101):
    arrow.dot(20, choice(color_list))
    arrow.forward(50)

    if dots % 10 == 0:
        arrow.setheading(90)
        arrow.forward(50)
        arrow.setheading(180)
        arrow.forward(500)
        arrow.setheading(0)

screen.exitonclick()