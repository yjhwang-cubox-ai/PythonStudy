from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle win?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

for idx, color in enumerate(colors):
    tim = Turtle(shape='turtle')
    tim.color(color)
    tim.penup()
    tim.goto(x=-230, y = -100 + 40*idx)
    turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    distance = random.randint(0,10)
    turtle = random.choice(turtles)
    
    turtle.forward(distance)
    
    if turtle.pos()[0] >= 250:
       if turtle.color()[0] == user_bet:
           print("you win!")
       else:
           print("you lose!")
       is_race_on = False
       
screen.exitonclick()