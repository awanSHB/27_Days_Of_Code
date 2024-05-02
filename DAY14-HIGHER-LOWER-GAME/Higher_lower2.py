import os
import random
from art import logo
from art import vs
from game_data import data
max = ''
def play_game_again():
    pass

def compare(p1, p2, user_input):
    f1 = p1['follower_count']
    f2 = p2['follower_count']
    if f1>f2:
        return user_input == 'a'

    elif f2>f1:
        return user_input == 'b'
    

def choosen():
    return random.choice(data)

def play_game_again():
    print(logo)
    person1 = choosen()
    person2 = choosen()
    score = 0
    keep_choosing = True
    while(keep_choosing):
        if score>0:
            person1 = person2
            person2 = choosen()
            if person1==person2:
                person2 = choosen()
        print()
        print(f"Compare A:- {person1['name']}, {person1['description']} from: {person1['country']}")
        print(vs)
        print(f"Compare B:- {person2['name']}, {person2['description']} from: {person2['country']}")
        user_choose = input("Choose the Option with highest followers: ").lower()
        os.system('cls')
        if compare(person1, person2, user_choose):
            score+=1
            print(f"Your score is: {score}")
        else:
            print()
            print("Sorry!!! That was the wrong Answer")
            print(f"Your score is: {score}")
            keep_choosing = False
play_game_again()

