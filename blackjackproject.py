logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from turtle import clear

"""return random card from deck"""


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def play_game(computer_score=None):
    global user_score
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #Hint 6: Create a function called calculate_score() that takes a List of cards as input
    #and returns the score.
    #Look up the sum() function to help you do this.
    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

    def calculate_score(cards):
        """Take a list of cards and return the score calculated from the cards"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)  #sum function adds the entities in list cards from left to right

    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score:{user_score}")
        print(f"Computer's first Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True


        #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as
    # long as it has a score less than 17.

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and
    # user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If
    # the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the
    # computer_score is over 21, then the computer loses. If none of the above, then the player with the highest
    # score wins.

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw"
        elif computer_score == 0:
            return "You lose, Computer has a blackjack"
        elif user_score == 0:
            return "You win, Its a blackjack"
        elif computer_score > 21:
            return "You win, Opponent went over 21"
        elif user_score > 21:
            return "You lose, Your score is over 21"
        elif user_score > computer_score:
            return "You win"
        else:
            return "you lose"

    print(f"Your final hand:{user_cards}, final score:{user_score}")
    print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the screen
while input("Do you want to play a game of blackjack? Type 'y' for yes or 'n' for no") == 'y':
    clear()
    play_game()
