import turtle as t

timmy = t.Turtle()
screen = t.Screen()

timmy.speed(0)


# Draw a yellow circle
timmy.color("black")
timmy.pensize(5)
timmy.penup()
timmy.pendown()


timmy.fillcolor("yellow")
timmy.begin_fill()
timmy.circle(100)
timmy.end_fill()
timmy.penup()

def eye(rad):
    timmy.pendown()
    timmy.color("black")
    timmy.fillcolor("black")
    timmy.begin_fill()
    timmy.circle(rad)
    timmy.end_fill()
    timmy.penup()

# Draw eyes
timmy.goto(-40, 120)
eye(15)
timmy.goto(40, 120)
eye(15)

# Draw mouth
timmy.pensize(5)
timmy.goto(-60, 95)
timmy.down()
timmy.right(90)
timmy.circle(60, 180)
timmy.up()

screen.exitonclick()
