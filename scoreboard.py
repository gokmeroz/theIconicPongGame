from turtle import Turtle
from paddle import Paddle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right=0
        self.left=0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right, align="center", font=("Courier", 80, "normal"))
    def lScore(self):
        self.left+=1
    def rScore(self):
        self.right+=1