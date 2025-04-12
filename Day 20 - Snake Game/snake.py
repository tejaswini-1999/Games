from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:    

    def __init__(self):
        
        self.segments = []
        self.positions = [(0, 0), (-20, 0), (-40, 0)]

        # Snake color, shape, size 
        for pos in self.positions:
            self.body(pos)
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def body(self, pos):
        new_seg = Turtle()
        new_seg.color("white")
        new_seg.shape("square")
        new_seg.penup()
        new_seg.setpos(pos)
        self.segments.append(new_seg)
            
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):        

        for x in range(len(self.segments) - 1, 0, -1):
            self.segments[x].setpos(self.segments[x-1].xcor(), self.segments[x-1].ycor())
        
        self.head.forward(MOVE_DISTANCE)    
    
    def extend(self):
        self.body(self.tail.position())      