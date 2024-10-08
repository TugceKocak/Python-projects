from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,coordinate):
        super().__init__()
        self.shape('square')
        self.shapesize(5,1)
        self.color('white')
        self.penup()
        self.goto(coordinate)

    def go_up(self):
        self.goto(self.xcor(),self.ycor()+20)

    def go_down(self):
        self.goto(self.xcor(),self.ycor()-20)
