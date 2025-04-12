from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed(0)

def forward():
    tim.forward(10)
def backward():
    tim.backward(10)
def right():
    tim.right(10)
def left():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.setpos(0, 0)
    tim.pendown()

screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(clear, "c")



screen.exitonclick()