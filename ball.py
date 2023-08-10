from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.home()
        self.color("white")
        self.x=10
        self.y=10


    def ballMovement(self):
        newX=self.xcor()+self.x
        newY=self.ycor()+self.y
        self.goto(newX,newY)
    def bounceY(self):
        self.y*=-1
    def bounceX(self):
        self.x*=-1
