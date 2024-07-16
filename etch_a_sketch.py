from turtle import Turtle, Screen

tee = Turtle()
screen = Screen()


def move_forward():
    tee.forward(10)


def move_backwards():
    tee.backward(10)


def turn_right():
    tee.right(10)


def turn_left():
    tee.left(10)


def clear():
    tee.clear()
    tee.home()
    tee.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(clear, "c")
screen.onkey(turn_right, "d")
screen.exitonclick()
