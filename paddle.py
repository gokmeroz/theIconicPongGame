from turtle import Turtle,Screen
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)
        self.score=0

    def goUp(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def goDown(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY)