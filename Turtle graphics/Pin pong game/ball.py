from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setposition(0, 0)
        self.move_speed=0.1
    def move(self,x_direction,y_direction):
        if y_direction == 'up' and x_direction == 'right':
            self.goto(self.xcor()+5,self.ycor()+5)
        elif y_direction == 'down' and x_direction == 'right':
            self.goto(self.xcor()+5,self.ycor()-5)
        elif y_direction == 'up'and x_direction == 'left':
            self.goto(self.xcor()-5,self.ycor()+5)
        elif y_direction == 'down'and x_direction == 'left':
            self.goto(self.xcor()-5,self.ycor()-5)