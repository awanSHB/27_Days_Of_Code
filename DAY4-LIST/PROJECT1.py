print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to the treasure island")
print("Your mission here is to find the treasure island")
choice1 = input("You are on the crossboard where do you want to go? type 'left' of 'right' : ")
if choice1=='right':
    choice2 = input("You have came to a lake and there is an island in the middle of the lake, if you want to wait for the boat type 'wait' otherwise 'swim' : ")
    if choice2=='wait':
        choice3 = input("You have arrived at the island unharmed. There are three doors 'red', 'blue' and 'yellow'. Which color would you like to choose : ")
        if choice3 == 'red':
            print("This roome is full of fire")
        elif choice3=='blue':
            print("Congratulations! you have found the treasure.")
        else:
            print("You entered into the room of beast...!Game Over!")
    else:
        print("You have got attacked by trout...!Game Over!")
else:
    print("Game over you have choosen the wrong side")