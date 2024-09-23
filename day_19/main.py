import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")

player = Player()
score = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    if random.randint(1, 3) == 1:
        car_manager.create_car()
        
    car_manager.move_cars()
    time.sleep(0.1)
    for car in car_manager.all_cars:
        if player.distance(car) < 27:
            score.game_over()
            game_is_on = False
    if player.ycor() > 280:
        player.restart()
        score.increase_score()
    screen.update()

screen.exitonclick()