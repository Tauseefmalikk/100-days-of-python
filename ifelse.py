print("welocme to the rollercoster")
height=int(input("What is your height in cm"))
bill=0
if height > 120:
    print("you can ride")
    age=int(input("what is your age?"))
    if age<12:
        bill=5
        print("Child tickets are $5")
    elif age <=18:
        bill=7
        print("Youth tickets are $7")
    else:
        bill=10
        print("Adult tickets are $10")
    photo=input("do you want photos yes or no?")
    if photo == "yes":
        bill = bill + 3
    print(f"your final bill = ${bill}")
    
else:
    print("You cant ride")