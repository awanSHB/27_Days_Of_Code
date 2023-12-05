import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'  """

print(logo)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
    
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
        
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You Lose! Both went over!!"
    elif user_score == computer_score:
        return "Draw!!!"
    elif user_score == 0:
        return "You Won! You have the blackjack"
    elif computer_score == 0:
        return "You lose! Computer has blackJack"
    elif user_score > 21:
        return "You Lose! You went over"
    elif computer_score > 21:
        return "You won! Computer went over"
    elif user_score > computer_score:
        return "You Won! Your score is high"
    else:
        return "You Lose"
        
def playing():
    user_cards = []
    computer_cards = []
    is_game_active = True
    
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while is_game_active:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards are: {user_cards}, Your score is: {user_score}")
        print(f"Computer's first card is: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_active = False
        else:
            user_play = input("Press z to draw another card, press x to pass: ")
            if user_play=='z':
                user_cards.append(deal_card())
            else:
                is_game_active = False
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"Your cards are: {user_cards}, Your score is: {user_score}")
    print(f"Computer cards are: {computer_cards}, Computer score is: {computer_score}")
    print(compare(user_score, computer_score))
while input("Do you want to Play? y for yes, n for no: ")=="y":
    playing()