from turtle import Turtle, Screen
from random import Random

screen = Screen()
screen.setup(500,400)
user_bet=screen.textinput("Make your bet","Which turtle will win the race? Enter a color:")
colors=["red","gold","blue","saddle brown","green","purple"]
turtle_list=[]
for i in range(6):
    tim=Turtle(shape='turtle')
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230,y=-100+i*35)
    turtle_list.append(tim)

r=Random()
race=True

while race:
    for tim in turtle_list:
        if tim.xcor()>230:
            winner_color=tim.pencolor()
            if winner_color==user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner")
            race=False
        tim.forward(r.randint(0,10))


screen.exitonclick()