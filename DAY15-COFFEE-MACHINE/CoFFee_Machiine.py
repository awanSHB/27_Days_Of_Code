menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
print('''
 _______  _______  _______  _______  _______  _______          
(  ____ \(  ___  )(  ____ \(  ____ \(  ____ \(  ____ \         
| (    \/| (   ) || (    \/| (    \/| (    \/| (    \/         
| |      | |   | || (__    | (__    | (__    | (__             
| |      | |   | ||  __)   |  __)   |  __)   |  __)            
| |      | |   | || (      | (      | (      | (               
| (____/\| (___) || )      | )      | (____/\| (____/\         
(_______/(_______)|/       |/       (_______/(_______/         
                                                               
 _______  _______  _______          _________ _        _______ 
(       )(  ___  )(  ____ \|\     /|\__   __/( (    /|(  ____ \\
| () () || (   ) || (    \/| )   ( |   ) (   |  \  ( || (    \/
| || || || (___) || |      | (___) |   | |   |   \ | || (__    
| |(_)| ||  ___  || |      |  ___  |   | |   | (\ \) ||  __)   
| |   | || (   ) || |      | (   ) |   | |   | | \   || (      
| )   ( || )   ( || (____/\| )   ( |___) (___| )  \  || (____/\\
|/     \||/     \|(_______/|/     \|\_______/|/    )_)(_______/
                                                               
''')
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

# Here we are printing the resources of the drink that user choosed
def taste(my_inp):
    print()
    print(f"You choose {my_inp} and it Recquires:  ")
    print(f"water  : {menu[my_inp]['ingredients']['water']}ml")
    print(f"milk   : {menu[my_inp]['ingredients']['milk']}ml")
    print(f"coffee : {menu[my_inp]['ingredients']['coffee']}ml")

# we are checking if the drink resources/requirement are greater than the our actual resources
# if drink resources are greater than it will become false and won't proceed
def resources_enough(ingred_order):
    for i in ingred_order:
        if ingred_order[i] >= resources[i]:
            print(f"SORRY!!! There are not enough Resources")
            return False
        return True


# we are taking the money from the user, different coins and adding them all to make total money received.
def coins_payment():
    print()
    print("Please Enter the coins")
    c1 = int(input("Enter the quarter: "))
    c2 = int(input("Enter the dime   : "))
    c3 = int(input("Enter the nickles: "))
    c4 = int(input("Enter the pennies: "))
    quart = c1*0.25
    dime = c2*0.1
    nickles = c3*0.05
    pennies = c4*0.01
    total = quart+dime+nickles+pennies
    return total

# we are doing the comaprison between drink cost and the money received
# if more money is received than we will return the extra money
def transaction(money_received, drink_cost):
    global profit
    print(f"\nThe money received: ${round(money_received, 2)}")
    print(f"The drink cost is : ${drink_cost}")
    if money_received > drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is ${change} in change")
        profit = profit+ drink_cost
        return True
    else:
        print("\nSORRY!!! You dont have enough money")
        return False

# we are deducing the actual resources(report) through resources of user choosen drink
def make_coffee(drink_name, order_ingredient):
    print()
    for i in order_ingredient:
        resources[i] = resources[i]-order_ingredient[i]
        print(f"{i} : {resources[i]}ml")
    print(f"\nYour Drink is : {drink_name}")

want_play = True
while(want_play):
    user_choice = input("Enter your choice espresso/latte/cappuccino, report, OFF: ").lower()
    if user_choice == "off":
        want_play = False
    elif user_choice == "report":
        print(f"\nWater  :{resources['water']}ml") 
        print(f"Milk   :{resources['milk']}ml") 
        print(f"Coffee :{resources['coffee']}ml")
        print(f"Money : ${profit}")
    else:
        drink = menu[user_choice]                   # it will print the drink's ingredients
        taste(user_choice)                          # calling the function of user choosen drink
        if resources_enough(drink['ingredients']):  # calling enough resources function true or not?
            payment = coins_payment()               # returning the total money user paid
            transaction(payment, drink['cost'])     # calling transaction function return extra money
            make_coffee(user_choice, drink['ingredients'])  # deducing actual resources