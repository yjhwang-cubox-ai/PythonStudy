from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()

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
    
screen.exitonclick()