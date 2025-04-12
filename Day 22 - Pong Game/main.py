from turtle import Turtle, Screen
from pong import Pong
from ball import Ball
from  score import Score
import time

LEFT = (-370, 0)
RIGHT = (370, 0)

screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


right_paddle = Pong(RIGHT)
left_paddle = Pong(LEFT)
ball = Ball()
score = Score()



screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

while True:
    screen.update()
    time.sleep(0.05)

    ball.move()
    
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    if (ball.distance(right_paddle.curr_position()) < 50 and ball.xcor() > 340) or (ball.distance(left_paddle.curr_position()) < 50 and ball.xcor() < -340):
        ball.collide()
    
    if ball.xcor() > 380 or ball.xcor() < -380:
        score.update_score(ball.xcor())
        ball.setpos(0, 0)
        ball.collide()
        ball.move_speed = 0.1





























screen.exitonclick()