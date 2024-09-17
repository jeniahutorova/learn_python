import turtle as t 

pen = t.Turtle()
screen = t.Screen()

def go_forward():
    pen.forward(50)

def go_backward():
    pen.backward(50)

def turn_clockwise():
    newheading = pen.heading() + 10
    pen.setheading(newheading)

def turn_counterclockwise():
    newheading = pen.heading() - 10
    pen.setheading(newheading)

def draw_circle():
    pen.circle(120,180)

def listener(key, func):
    screen.onkey(func,key)

def clearscreen():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()

screen.listen()

listener("w", go_forward)
listener("s", go_backward)
listener("d", turn_clockwise)
listener("a", turn_counterclockwise)
listener("c", clearscreen)
screen.exitonclick()

