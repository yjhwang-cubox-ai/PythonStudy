import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r, g, b)


directions = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed("fastest")

t.setup(width=1500, height=1500)

def draw_spirograph(angle):
    for _ in range(int(360/angle)):
        tim.color(random_color())
        tim.circle(100)
        tim.right(angle)

draw_spirograph(10)
        