import turtle as t
import random

tee = t.Turtle()
colors = ["red", "blue", "orange", "pink", "black", "green", "yellow", "aquamarine"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tee.forward(100)
        tee.right(angle)


for shape_side_n in range(3, 11):
    tee.color(random.choice(colors))
    draw_shape(shape_side_n)
