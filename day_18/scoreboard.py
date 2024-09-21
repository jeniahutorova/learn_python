from turtle import Turtle
FONT = ("Arial", 30, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
    
    def left_score_up(self):
        self.l_score += 1
        self.update_score() 
    
    def right_score_up(self):
        self.r_score += 1
        self.update_score() 
