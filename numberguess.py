from random import randint
logo="""  ________                             ___________.__              _______               ___.                 
 /  _____/ __ __  ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  |  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/ \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/           \/     \/     \/                  \/     \/          \/            \/    \/     \/       """

print(logo)

Easy_level_turns=10
Hard_level_turns=5

def check_answer(guess,answer,turns):
    """Checks answer against guess and returns the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You go it! The answer was{answer}")
        
        
def set_difficulty():
    level=input("Choose a difficulty> Type 'easy' or 'hard':")
    if level=="easy":
        return Easy_level_turns
    else:
        return Hard_level_turns

def game():
    #chosing a random number between 1 and 100
    print("welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100..")
    answer = randint(1,100)
    print(f"{answer}")


    turns=set_difficulty()
    

    guess=0
    while guess !=answer:
        print(f"you have {turns} attempts remaing to guess the number.")
        guess=int(input("Make a guess: "))
        turns= check_answer(guess,answer,turns)
        if turns == 0:
            print("You have run out of guesses, You lose")
            return
game()