from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.create_car()
        self.move_cars()
        self.increase_speed()
    
    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        random_y = random.randint(-240, 240)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.move_distance
            car.goto(new_x, car.ycor())

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
