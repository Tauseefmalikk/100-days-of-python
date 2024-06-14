
import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids={} #dictionary
bidding_finished=False

def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    #bidding_record={"angela":123,"james":321}
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The Winner is {winner} with a bid of ${highest_bid}")
    
    

while not bidding_finished:
    name=input("What is your name?")
    price=int(input("what is your bid? $"))
    bids[name]=price #adding key as name and price as value in bid dictionary
    should_continue=input("Are there any other bidders? type yes or no.\n")
    if should_continue=="no":
        bidding_finished=True
        find_highest_bidder(bids)
    elif should_continue=="yes":
        os.system('cls')