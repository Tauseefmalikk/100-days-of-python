#we can create as many as turtle objects from turtle class
import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
print(user_bet)

y_positions = [-80, -40, 0, 40, 80]
turtle_color = ["orange", "blue", "red", "pink","black"]
all_turtle = []


for i in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color[i])
    new_turtle.penup()
    new_turtle.goto(x=-210, y=y_positions[i])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won! The {winning_color} turtle is the winner")
            else:
                print(f"you have lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


# tommy = Turtle(shape="turtle")
# tommy.color("pink")
# tommy.penup()
# tommy.goto(x=-210, y=0)
#
# roo = Turtle(shape="turtle")
# roo.color("blue")
# roo.penup()
# roo.goto(x=-210, y=40)

# roo.color("blue")


screen.exitonclick()
