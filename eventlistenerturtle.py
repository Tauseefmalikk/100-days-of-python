from turtle import Turtle, Screen

tee = Turtle()
screen = Screen()


def move_forward():
    tee.forward(20)


screen.listen()
screen.onkey(key="space", fun=move_forward)  #we can control our turtle with keys strokes
screen.exitonclick()
