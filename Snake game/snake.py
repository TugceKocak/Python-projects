from turtle import Turtle
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.snake_parts = []
        for i in range(3):
            self.add_snake_part((-20*i,0))

        self.head=self.snake_parts[0]
    def add_snake_part(self,position):
        tim = Turtle("square")
        tim.color('white')
        tim.shapesize(1)
        tim.penup()
        tim.goto(position)
        self.snake_parts.append(tim)

    def extend(self):
        self.add_snake_part(self.snake_parts[-1].position())

    def move(self):
        for i in range(len(self.snake_parts) - 1, 0, -1):
            x, y = self.snake_parts[i - 1].pos()
            self.snake_parts[i].goto(x, y)
        self.snake_parts[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

