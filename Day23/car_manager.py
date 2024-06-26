from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.carlist = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def make_car(self):
        if random.random() > 0.8:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250, 250))
            self.carlist.append(new_car)
        else:
            pass
        
    def move_cars(self):
        for car in self.carlist:
            car.forward(MOVE_INCREMENT)
        if len(self.carlist) > 0 and self.carlist[0].xcor() < -350:
            del self.carlist[0]
    
    def car_speedup(self):
        self.car_speed += MOVE_INCREMENT