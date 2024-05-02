import random
logo = '''
 _____                    _____ _          _____           _           
|   __|_ _ ___ ___ ___   |_   _| |_ ___   |   | |_ _ _____| |_ ___ ___ 
|  |  | | | -_|_ -|_ -|    | | |   | -_|  | | | | | |     | . | -_|  _|
|_____|___|___|___|___|    |_| |_|_|___|  |_|___|___|_|_|_|___|___|_|
'''
print(logo)

def result():
    global user_guess
    user_guess = int(input("Guess the number: "))
    if user_guess < computer_guess:
        print("Number is low")
    elif user_guess > computer_guess:
        print("Guess is high")
    elif user_guess ==computer_guess:
        print(f"Bravo!! You got it Your guess '{user_guess}' == '{computer_guess}'")

computer_guess = random.randint(1, 101)
print("I am thinking about a numbee between 1-100")
level = input("Which level would you like to play?: Easy, Medium or Hard?: ")
if level=="easy":
    for life in range(14):
        result()
        if user_guess ==computer_guess:
            break
        guesses = 13-life
        print(f"Your remaining guesses are {guesses}")
    if user_guess == computer_guess:
        print("You Won the game")
    else:
        print("You lost the game")
        print(f"The number was {computer_guess}")

elif level=="medium":
    for life in range(9):
        user_guess = int(input("Guess the number: "))
        result()
        if user_guess ==computer_guess:
            break
        guesses = 8-life
        print(f"Your remaining guesses are {guesses}")
    if user_guess == computer_guess:
        print("You Won the game")
    else:
        print("You lost the game")
        print(f"The number was {computer_guess}")
elif level=="hard":
    n = 6
    for life in range(n):
        user_guess = int(input("Guess the number: "))
        result()
        if user_guess ==computer_guess:
            break
        guesses = (n-1)-life
        print(f"Your remaining guesses are {guesses}")
    if user_guess == computer_guess:
        print("You Won the game")
    else:
        print("You lost the game")
        print(f"The number was {computer_guess}")