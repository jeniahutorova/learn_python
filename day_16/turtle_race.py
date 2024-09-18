import turtle as t
import random

race_is_on = False
screen = t.Screen()
screen.setup(500, 400)

color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-90, -50, -10, 30, 70, 110]

user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

turtle_list = []

for turtle_index in range(0, 6):
    tim = t.Turtle(shape="turtle")
    tim.penup()
    tim.goto(-230, y_positions[turtle_index])
    tim.pendown()
    tim.color(color[turtle_index])
    turtle_list.append(tim)

if user_bet.lower():
    race_is_on = True

while race_is_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose! The {winning_color} turtle is the winner!")
        turtle.penup()
        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)
    
screen.exitonclick()