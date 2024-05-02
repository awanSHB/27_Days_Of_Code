import os
import random
from art import logo
from art import vs
from game_data import data

def compare(p1, p2, user_input):
    f1 = p1['follower_count']
    f2 = p2['follower_count']
    if f1>f2:
        if user_input=="a":
            return True
    elif f2>f1:
        if user_input=="b":
            return True
try_again = True
while(try_again):
    def play_game():
        print(logo)
        score = 0
        person1 = random.choice(data)
        person2 = random.choice(data)
        keep_choosing = True
        while(keep_choosing):
            if person1 == person2:
                person2 = random.choice(data)
            if score>0:
                person1 = person2
                person2 = random.choice(data)
                if person1 == person2:
                    person2 = random.choice(data)
            
            print(f"A:- {person1['name']}, {person1['description']} From : {person1['country']}")
            print(vs)
            print(f"B:- {person2['name']}, {person2['description']} From : {person2['country']}")
            guess = input("Choose the option with highest followers: ").lower()
            os.system('cls')
            if compare(person1, person2, guess):
                score+=1
                print("------------------------")
                print(f"   Your score is: {score}")
                print("------------------------")
            else:
                print("Sorry!!! That was the poor choice")
                print("------------------------")
                print(f"   Your score is: {score}")
                print("------------------------")
                keep_choosing = False
    play_game()
    ch = input("Do you want to try again?: Press y, else press n:- ")
    if ch=="n":
        try_again = False