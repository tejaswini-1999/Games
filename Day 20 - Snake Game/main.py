from turtle import Screen
from snake import Snake
from  food import Food
from score import Score
import time

EDGE = 290

screen = Screen()


# Setting up the screen
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)   

    snake.move() 

    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend()
    
    if (snake.head.xcor() > EDGE or snake.head.xcor() < -EDGE
        or snake.head.ycor() > EDGE or snake.head.ycor() < -EDGE):
        game_is_on = False
        score.gameover()
    
    for segment in snake.segments[1 : len(snake.segments)]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.gameover()

screen.exitonclick()