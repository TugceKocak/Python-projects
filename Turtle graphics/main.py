import random
import turtle
from turtle import Turtle,Screen

timmy=Turtle()
timmy.color("goldenrod")
timmy.pensize(2)
timmy.speed(14)
turtle.colormode(255)

def draw_square():
    for i in range(4):
        timmy.forward(100)
        timmy.right(90)

def draw_dashed_line():
    for i in range(10):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

def draw_complex_shape():
    for i in range(3,10):
        timmy.color(random.choice(colours))
        for j in range(i):
            timmy.forward(100)
            timmy.right(360//i)

def draw_random_walk():
    while True:
        timmy.color(random_color())
        timmy.forward(30)
        direction=random.choice([0,90,180,270])
        timmy.right(direction)

def draw_spirograph(gap_size,radius):
    for i in range(360//gap_size):
        timmy.color(random_color())
        timmy.circle(radius)
        timmy.setheading(timmy.heading()+gap_size)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tup=(r,g,b)
    return tup

draw_spirograph(20,70)
screen=Screen()
screen.exitonclick()

