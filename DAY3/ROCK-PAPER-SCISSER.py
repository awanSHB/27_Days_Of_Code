import random

rock = """
     rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
R = 'rock'
P = 'paper'
S = 'scissor'
image = [rock, paper, scissor]
imagee = [R, P, S]

print("Whar do you want to choose? :")
print("1-rock")
print("2-paper")
print("3-scissor")
user_choice = int(input("Enter your choice:>: "))
print(image[user_choice-1])
print()

computer_choice = random.randint(1, 3)
print("Computer has choosed :>: ")
print(image[computer_choice-1])
print()
a = imagee[user_choice-1]
b = imagee[computer_choice-1]

if user_choice >3 and user_choice <=0:
    print("You have enter an invalid command")
elif user_choice==1 and computer_choice==3:
    print("!!You won!!")
    print("Rock beat Scissor")
elif user_choice==3 and computer_choice==1:
    print("!!You Lose!!")
    print(f"Rock beat Scissor")
elif user_choice < computer_choice:
    print("!!You Lose!!")
    print(f"{b} beat {a}")
elif user_choice > computer_choice:
    print("!!You Won!!")
    print(f"{a} beat {b}")
elif user_choice == computer_choice:
    print("!!!!Game Draw!!!!")