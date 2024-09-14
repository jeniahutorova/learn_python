import turtle as t

timmy = t.Turtle()
timmy.shape("arrow")
timmy.color("chartreuse4")

# Makes a square
# for _ in range(1,5):
#     timmy.forward(100)
#     timmy.left(90)

# Makes a dotted line
# Method 1
# for _ in range(15):
#     timmy.forward(10)
#     timmy.color("white")
#     timmy.forward(15)
#     timmy.color("black")

# Method 2 
for _ in range(15):
    timmy.forward(10)
    timmy.pendown()
    timmy.forward(15)
    timmy.penup()
my_screen = t.Screen()
my_screen.exitonclick()                                                                                                                                                                                                                                                                                                                                                                                    