#This is a global scope
enemy = "alien"
def my_enemies():
    print()
    #This is a local scope
    enemy = "Monster"
    print(f"My local enemy is {enemy}")
my_enemies()
print(f"My global enemy is {enemy}")
print()

enemy = 1
def enemies():
    print(f"My enemies are {enemy}")
    return enemy+1
enemy = enemies()
print(f"My enemies are {enemy}")