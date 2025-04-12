from turtle import Turtle

SCORE_POSITION = (0, 240)
CENTER = "center"
FONT_SIZE = 30
FONT_TYPE = "Courier"

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(SCORE_POSITION)
        self.right_score = 0
        self.left_score = 0
        self.update_score(0)
        self.line_func()

    def line_func(self):
        line = Turtle()
        line.hideturtle()
        line.color("white")
        line.shape("square")
        line.penup()
        line.right(90)
        line.pensize(6)
        line.hideturtle()
        line.setpos(0, 285)

        while line.ycor() > - 280:
            line.pendown()
            line.forward(20)
            line.penup()
            line.forward(20)

    def update_score(self, y_cood):
        self.clear()
        if y_cood < -380:
            self.right_score += 1
        elif y_cood > 380:
            self.left_score += 1   
        
        self.write(f"{self.left_score} : {self.right_score}", align = CENTER, font = (FONT_TYPE, FONT_SIZE, "normal"))
        