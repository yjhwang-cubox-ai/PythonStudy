from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Right", fun=snake.turn_right)

game_is_on = True
while game_is_on:    
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.plus_score()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()
            
screen.exitonclick()