import turtle
import turtle as t
import random

directions = [0, 90, 180, 100]
tee = t.Turtle()
t.colormode(255)
tee.pensize(20)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for i in range(200):
    tee.color(random_color())
    tee.forward(30)
    tee.setheading(random.choice(directions))
