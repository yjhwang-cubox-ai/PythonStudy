import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.make_car()
    car_manager.move_cars()    
    
    for car in car_manager.carlist:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    if player.check_fline():
        scoreboard.up_score()
        player.reset()
        car_manager.car_speedup()
    
    screen.update()

screen.exitonclick()
