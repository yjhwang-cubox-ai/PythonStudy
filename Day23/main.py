from turtle import Screen
from bar import Bar
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ping-pong")
screen.tracer(0)

bar1 = Bar((350,0))
bar2 = Bar((-350,0))


screen.listen()
screen.onkey(key="Up", fun=bar1.move_up)
screen.onkey(key="Down", fun=bar1.move_down)
screen.onkey(key="w", fun=bar2.move_up)
screen.onkey(key="s", fun=bar2.move_down)

while True:
    screen.update()

screen.exitonclick()