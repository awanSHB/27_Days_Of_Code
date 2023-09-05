import random

words_list = ['horse', 'camel', 'elephant', 'baboon', 'monkey']

# randomly choose a word from the words_list and assign it to a variable
choosen = random.choice(words_list)
print(choosen)

# create an empty list with a display
display = []
st = "-"
# now assign the number of "-" in the display according to choosen word's letters.

for ch in range(len(choosen)):
    display += '-'
end_game = False

while end_game == False:
    # Take the input from the user and check and assigns that to a variable.
    guess = input("\nGuess the letter : ").lower()
    print()
    for ap in range(len(choosen)):
        if choosen[ap] == guess:
            display[ap] = choosen[ap]
    print(display)
    
    if '-' not in display:
        end_game = True
        print("--You Won--")