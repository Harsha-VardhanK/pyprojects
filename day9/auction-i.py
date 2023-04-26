import os
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    # bidding_record = {"Angela":123, "james: 435"}
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")



while not bidding_finished:

    name = input("What is your Name? :")
    price = int(input("What is your bid Price $:"))
    bids[name] = price
    should_continue = input("Are there any bidders? Type 'yes' or 'no' \n" )
    if should_continue == 'no':
       bidding_finished = True
       find_highest_bidder(bids)
    elif should_continue == 'yes':
        os.system('cls')
        #        continue
