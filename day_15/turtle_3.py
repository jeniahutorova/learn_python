import turtle as t
import random

t.colormode(255)
turn = ["left", "right", "forward", "back"]
color = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "cyan"]

timmy = t.Turtle()
screen = t.Screen()

# Well, not really what I wanted, but it's still going a different directions
# for _ in range(50):
#     direction = random.choice(turn)
#     timmy.pencolor(random.choice(color))
#     if direction == "left":
#         timmy.left(15)
#     elif direction == "right":
#         timmy.right(15)
#     elif direction == "forward":
#         timmy.forward(15)
#     elif direction == "back":
#         timmy.back(15)

# Option 2
# directions = [0, 90, 180, 360]
# for _ in range(200):
#     timmy.pencolor(random.choice(color))
#     timmy.pensize(20)
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
# screen.exitonclick()

# Option 3
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 360]
for _ in range(200):
    timmy.pencolor(random_color())
    timmy.pensize(20)
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
    timmy.speed("fastest")
screen.exitonclick()