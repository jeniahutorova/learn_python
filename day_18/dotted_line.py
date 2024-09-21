from turtle import Turtle

class Dotted_Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(3)
        self.draw_dotted_line()

    def draw_dotted_line(self):
        self.penup()
        self.goto(0,-300)
        self.setheading(90)
        self.color("white")
        for _ in range(25):
            self.forward(10)
            self.pendown()
            self.forward(15)
            self.penup()