from turtle import Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score=0
        self.right_score=0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100,225)
        self.write(self.left_score, align='center', font=('Courier', 50, 'normal'))
        self.goto(100,225)
        self.write(self.right_score, align='center', font=('Courier', 50, 'normal'))

    def l_point(self):
        self.left_score+=1
        self.update()

    def r_point(self):
        self.right_score+=1
        self.update()