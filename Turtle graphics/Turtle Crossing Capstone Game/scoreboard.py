FONT = ("Courier", 16, "bold")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.goto(-180, 250)
        self.write(f"Level: {self.score}", align="right", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)