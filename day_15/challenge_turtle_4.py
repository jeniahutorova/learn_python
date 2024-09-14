import turtle as t 
import random 

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

timmy = t.Turtle()
screen = t.Screen()

# Option 1
# for _ in range(200):
#     timmy.pencolor(random_color())
#     timmy.speed("fastest")
#     timmy.circle(100)
#     timmy.left(10)

# Option 2
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.pencolor(random_color())
        timmy.speed("fastest")
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
draw_spirograph(5)
screen.exitonclick()