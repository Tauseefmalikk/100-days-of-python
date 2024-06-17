# in oops, we are trying to model real world problems or objects and these objects
# have things  called attributes and can also do things called methods
from turtle import *

# tee = Turtle()
# print(tee)
# tee.shape("turtle")
# tee.color('red')
# tee.forward(100)
# screen = Screen()
# print(screen.canvheight)
# screen.exitonclick()

#
# accessing package prettytable

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["pikachu", "Charmelon", "Maril"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
