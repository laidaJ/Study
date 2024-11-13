import os
from ascii_art import logo

print(logo)

bids_dictionary = {}

def add_bid(new_name, new_bid):
    os.system('clear')
    bids_dictionary[new_name] = new_bid

def end_bid():
    high_bid = 0
    high_name = ""
    for bid_name in bids_dictionary:
        if bids_dictionary[bid_name] > high_bid:
            high_name = bid_name
            high_bid = bids_dictionary[bid_name]
    print(f"Highest bid is {high_name} bid ${high_bid}")


continue_bid = True
while continue_bid:
    name = input("Type your name:\n")
    bid = int(input("Type your bid:\n"))
    bid_or_not = input("Others want to bid? Type(Y/N):").lower()
    add_bid(new_name=name, new_bid=bid)
    if bid_or_not == "y":
        continue_bid = True
    else:
        continue_bid = False
        end_bid()
