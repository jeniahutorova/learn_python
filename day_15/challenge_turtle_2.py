import turtle as t
import random

timmy = t.Turtle()
timmy.shape("arrow")
screen = t.Screen()

colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "cyan"]
for number_of_sides in range(3, 10):
    timmy.pencolor(random.choice(colors))
    turn = 360/number_of_sides
    for _ in range(number_of_sides):
        timmy.forward(100)
        timmy.right(turn)
screen.exitonclick()

