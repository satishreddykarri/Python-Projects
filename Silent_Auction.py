import os
def find_winner(bidders_data):
    highest_bid =0
    winner = ""
    for bidder in bidders_data:
        bidding_price = bidders_data[bidder]
        if(bidding_price>highest_bid):
            highest_bid = bidding_price
            winner = bidder
    print(bidders_data)
    print(f"THis winner is {winner} with a bid of {highest_bid}")

print("**************WELCOME TO SILENT AUCTION PROGRM*****************")
bidders = False
bidding_dict = {}
while not bidders:
    name = input("What is your name?? ")
    bid_amount = int(input("What is you bid?? "))
    asking = input("Are there any other bidders(type 'yes' for continue 'no' to stop): ")
    bidding_dict[name] = bid_amount
    if asking == 'no':
        bidders = True
        find_winner(bidding_dict)
    elif asking == 'yes':
       os.system('cls')
