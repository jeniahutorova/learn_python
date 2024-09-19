from turtle import Turtle, Screen
import time
from snake import Snake

pen = Turtle()
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()

game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_is_on:
    screen.update() # Updates screen after loop is finished
    time.sleep(0.1)
    
    snake.move()

screen.exitonclick()