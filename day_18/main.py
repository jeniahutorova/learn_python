from turtle import Screen
from paddle import Paddle
from dotted_line import Dotted_Line
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.title("Pong game")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
dotted_line = Dotted_Line()
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if  (ball.xcor() < -320 and ball.distance(left_paddle) < 30) or ( ball.xcor() > 320 and ball.distance(right_paddle) < 30):
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_score_up()
    
    if ball.xcor() < -380:
        ball.reset_position()
        score.right_score_up()

        


    
screen.exitonclick()