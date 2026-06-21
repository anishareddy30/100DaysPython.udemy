import secret_auction_art
print("welcome to the secret auction ")

print(secret_auction_art.logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0 
    winner = ""
    for bidding in bidding_record :
        bid_price = bidding_record[bidding]
        if bid_price > highest_bid :
            highest_bid = bid_price
            winner = bidding
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
bid_continue = True
while bid_continue :
    name = input("whats your name ?")
    bid_price = int(input("whats the bid price ? "))
    bids[name] = bid_price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if should_continue == "no":
        bid_continue = False
        find_highest_bidder(bids)
    elif should_continue == "yes": 
        print("\n" * 20)
