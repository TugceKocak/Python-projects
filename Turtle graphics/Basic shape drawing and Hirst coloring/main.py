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

def draw_hirstcolor():
    # color_list=[]
    # colors = colorgram.extract('hirst_image.jpg', 25)
    # for color in colors:
    #     tup=(color.rgb[0], color.rgb[1], color.rgb[2])
    #     color_list.append(tup)
    # print(color_list)

    # color_list is derived from the color palette in the hirst image
    color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
                  (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36),
                  (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151),
                  (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

    timmy.hideturtle()
    timmy.penup()
    timmy.setposition(-250, -250)

    for i in range(10):
        for j in range(10):
            timmy.dot(20, random.choice(color_list))
            timmy.fd(50)
        x, y = timmy.pos()
        timmy.setposition(-250, y + 50)

draw_hirstcolor()
screen=Screen()
screen.exitonclick()

