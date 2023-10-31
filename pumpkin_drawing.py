# Pumpkin Drawing
# Author: Brant
# Date: 31 October 2023

import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()
carver.speed(5)  # Setting speed to a medium pace for visibility
carver.color("black")
carver.hideturtle()  # Hide the turtle cursor

# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-100, -100)
carver.pensize(60)
carver.pendown()
carver.forward(200)
carver.pensize(2)

# Eyes
def draw_eye(x, y):
    carver.penup()
    carver.setposition(x, y)
    carver.pendown()
    carver.begin_fill()
    carver.circle(20, 180)  # Half circle for a spooky look!
    carver.left(90)
    carver.forward(40)
    carver.left(90)
    carver.circle(20, 180)
    carver.end_fill()

draw_eye(-50, 20)
draw_eye(50, 50)

# Nose
carver.penup()
carver.setposition(0, 20)
carver.pendown()
carver.begin_fill()
carver.circle(-15, 180)  # Small upside-down half-circle
carver.end_fill()

# Mouth
carver.penup()
carver.setposition(-50, -30)
carver.pendown()
carver.begin_fill()
carver.setheading(-60)  # Pointing downwards
carver.circle(50, 120)  # Wide creepy smile
carver.end_fill()

turtle.done()
