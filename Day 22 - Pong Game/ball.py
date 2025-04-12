from turtle import Turtle

BALL_POSITION = (0, 0)
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setpos(BALL_POSITION)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)
    
    def bounce(self):
        self.y_move *= -1

    def collide(self):
        self.x_move *= -1
        self.move_speed *= 0.9

            
