from turtle import Turtle, Screen

CENTER = "center"
FONT_SIZE = 24
SCORE_POSITION = (0, 275)

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.setpos(SCORE_POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}", align = CENTER, font = (FONT_SIZE))
        self.score += 1
        
    def gameover(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align = CENTER, font = (FONT_SIZE))