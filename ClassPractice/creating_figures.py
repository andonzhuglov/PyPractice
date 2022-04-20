from turtle import Turtle, Screen
screen = Screen()
screen.bgcolor("black") #background color to black

arrow = Turtle()
arrow.color("purple2") #changes the color of the pen
arrow.pensize(2) #bolded with size 2
arrow.ht() #hides the arrow


def draw_shape(num_sides):
    '''Takes number of sides and draws a figure'''
    angle = 360 / num_sides
    for x in range(num_sides):
        arrow.forward(100)
        arrow.right(angle)


for sides in range(3, 11):
    draw_shape(sides)

screen.exitonclick()