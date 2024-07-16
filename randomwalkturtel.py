import turtle
import turtle as t
import random

tee = t.Turtle()
colors = ["red", "blue", "orange", "pink", "black", "green", "yellow", "aquamarine"]
directions = [0, 90, 100, 180]
tee.pensize(12)
turtle.speed("slow")
for i in range(200):
    tee.color(random.choice(colors))
    tee.forward(30)
    tee.setheading(random.choice(directions))
