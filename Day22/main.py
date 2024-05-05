from turtle import Screen
from bar import Bar
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ping-pong")
screen.tracer(0)

bar_right = Bar((350,0))
bar_left = Bar((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=bar_right.move_up)
screen.onkey(key="Down", fun=bar_right.move_down)
screen.onkey(key="w", fun=bar_left.move_up)
screen.onkey(key="s", fun=bar_left.move_down)

is_game_on = True
while is_game_on:
    ball.move()
    
    if ball.y_pos >= 290 or ball.y_pos <= -290:
        ball.bounce()
        
    if (ball.xcor() > 330 and ball.distance(bar_right) < 50) or (ball.xcor() < -330 and ball.distance(bar_left) < 50):
        ball.bounce_bar()
    
    if ball.xcor() >= 390:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() <= -390:
        ball.reset_position()
        scoreboard.r_point()
    
    screen.update()
    time.sleep(ball.move_speed)

screen.exitonclick()