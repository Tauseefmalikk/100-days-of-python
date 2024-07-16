import turtle as t
import random

directions = [0, 90, 180, 100]
tee = t.Turtle()
t.colormode(255)
tee.pensize(2)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tee.speed("fastest")


def draw(size):
    for i in range(int(360 / size)):
        tee.color(random_color())
        tee.circle(100)
        current_heading = tee.heading()
        tee.setheading(current_heading + size)
        tee.circle(100)


draw(6)

screen = t.Screen()
screen.exitonclick()
