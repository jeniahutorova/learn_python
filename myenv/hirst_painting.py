# import colorgram

# colors = colorgram.extract("/Users/jane/learn_python/myenv/dot_painting.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors_tuple = (r, g, b)
#     rgb_colors.append(rgb_colors_tuple)

# print(rgb_colors)

import turtle as t
import random

t.colormode(255)

cursor = t.Turtle()
cursor.speed(0)
screen = t.Screen()
color_list = [(207, 159, 82), (54, 89, 130), (146, 91, 39), (140, 26, 48), (222, 207, 104), (132, 177, 203), (158, 46, 83), (45, 55, 104), (170, 160, 39), (129, 189, 143), (83, 20, 44), (36, 43, 69), (186, 94, 106), (186, 140, 172), (84, 120, 180), (60, 39, 31), (88, 157, 92), (78, 153, 164), (195, 78, 72), (45, 74, 78), (80, 74, 44), (162, 201, 218), (58, 126, 122), (218, 176, 187), (169, 207, 170), (220, 181, 168)]

cursor.penup()
cursor.setheading(225)
cursor.forward(300)
cursor.setheading(0)

circles_per_row = 10 

for _ in range(10):
    for circle in range(circles_per_row):
        color = random.choice(color_list)
        cursor.pencolor(color)
        cursor.fillcolor(color)

        cursor.begin_fill()
        cursor.circle(20)
        cursor.end_fill()

        cursor.penup()
        cursor.forward(50)
        cursor.pendown()


    cursor.penup()
    cursor.setheading(90)  # Point up
    cursor.forward(50)  # Move up to the next row
    cursor.setheading(180)  # Point left
    cursor.forward(500)  # Move to the start of the row
    cursor.setheading(0)  # Reset direction to right
    cursor.pendown()

screen.exitonclick()