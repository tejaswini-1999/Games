from turtle import Turtle
import random

FOOD_EDGE = 270

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.setpos(random.randint(-FOOD_EDGE, FOOD_EDGE), random.randint(-FOOD_EDGE, FOOD_EDGE))