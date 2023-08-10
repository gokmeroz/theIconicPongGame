from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle1=Paddle((350,0))
paddle2=Paddle((-350,0))
ball = Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(paddle1.goUp,"Up")
screen.onkey(paddle1.goDown,"Down")
screen.onkey(paddle2.goUp,"w")
screen.onkey(paddle2.goDown,"s")

isGameOver=False
while not isGameOver:
    time.sleep(0.05)
    screen.update()
    ball.ballMovement()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
    if ball.xcor() > 380:
        scoreboard.lScore()
        scoreboard.update()
        ball.home()
    elif  ball.xcor() < -380:
        scoreboard.rScore()
        scoreboard.update()
        ball.home()
    if ball.distance(paddle1) < 60 and ball.xcor()>340 or ball.distance(paddle2) < 60 and ball.xcor() < -340:
        ball.bounceX()

screen.exitonclick()