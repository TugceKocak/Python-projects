COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars=[]
        self.hideturtle()
        self.speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        number=random.randint(1,6)
        if number == 1:
            car=Turtle("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(1, 2)
            car.setposition(300, random.randint(-240, 280))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed+=MOVE_INCREMENT