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
bids = {}
def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'\nThe winner is :  "{winner}"  : with the highest bid of :  "${highest_bid}"')
game_finished = False
while not game_finished:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $"))
    bids[name] = price
    keep_going = input('Is there any other player?: "yes"? or "no"?: ')
    if keep_going == 'no':
        game_finished = True
        highest_bidder(bids)
    elif keep_going == 'yes':
        os.system('cls')
            