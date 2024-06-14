import random
names=["Tauseef","fazeem","Shadab","Faheem"]

items=len(names)
random_choice=random.randint(0,items-1)
persontopay=names[random_choice]
print(persontopay + " is going to buy the meal today")