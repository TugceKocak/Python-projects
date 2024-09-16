import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(fun=player.move,key="Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    #Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

    # detect when turtle reaches the other side
    if player.is_at_finish_line():
        car_manager.level_up()
        scoreboard.update_score()

screen.exitonclick()