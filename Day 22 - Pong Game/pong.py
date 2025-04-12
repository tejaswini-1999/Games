from turtle import Turtle

LEFT = (-350, 0)
RIGHT = (350, 0)

class Pong:
    def __init__(self, pos):
        self.paddle = Turtle()
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.left(90)
        self.paddle.shapesize(1, 5)
        self.paddle.penup()
        self.paddle.setpos(pos)

    
    def up(self):
        self.paddle.forward(30)


    def down(self):
       self.paddle.backward(30)
    
    def curr_position(self):
        return(self.paddle.position())