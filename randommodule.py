import random  #random module
import mymodule #importing my module

random_integer=random.randint(1,10)
print(random_integer)

random_float=random.random()
print(random_float)

#heads or tails
toss=random.randint(0,1)
if toss == 0:
    print("Tails")
else:
    print("Heads")