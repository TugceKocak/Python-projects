from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier", 16,'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.write(f"Score:  {self.score}", False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score:  {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, align=ALIGNMENT, font=FONT)