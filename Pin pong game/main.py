from turtle import Turtle,Screen
from ball import Ball
from paddle import Paddle
import time
from score_board import Score_board

tim=Turtle()
screen=Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

right_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Score_board()

screen.listen()
screen.onkey(fun=right_paddle.go_up,key="Up")
screen.onkey(fun=right_paddle.go_down,key="Down")

screen.onkey(fun=left_paddle.go_up,key="W")
screen.onkey(fun=left_paddle.go_down,key="S")

game_is_on=True
y_direction="up"
x_direction="right"
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move(x_direction,y_direction)

    # detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        if y_direction=="up": y_direction="down"
        else: y_direction="up"

    # detect collision with r_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor()>330:
        x_direction="left"
        ball.move_speed*=0.9
    if ball.distance(left_paddle) < 50 and ball.xcor()<-330:
        x_direction="right"
        ball.move_speed *=0.9

    #detect when paddle misses
    if ball.xcor() > 350 or ball.xcor() < -350:
        ball.setposition(0,0)
        ball.move_speed=0.1
        if x_direction=="right":
            x_direction="left"
            scoreboard.l_point()
        else:
            x_direction="right"
            scoreboard.r_point()
        y_direction="up"
screen.exitonclick()