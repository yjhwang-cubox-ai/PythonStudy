import colorgram
import turtle as t
import random

colors = colorgram.extract('img.jpg',50)

color_list = []
for color in colors:
    color = color.rgb
    r = color[0]
    g = color[1]
    b = color[2]
    
    color_tuple = (r, g, b)
    color_list.append(color_tuple)

tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
t.colormode(255)
# t.setup(width=500, height=500)

for idx in range(101):

    tim.dot(20, random.choice(color_list))
    # tim.penup()
    tim.fd(50)

    if idx % 10 == 0:
        tim.setpos(0, idx*5)