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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO: 1. User input asking the menu
# TODO: 2. Turning off for maintenance
# TODO: 3. Check resources using report
# TODO: 4. Check enough resources to make coffee

profit = 0

def enough_resources(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry! There are not enough {items}")
            return False
        return True

def process_coins():
    print("Please insert the coins: ")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total

def transaction(money_received, drink_cost):
    if money_received > drink_cost:
        ch = round(money_received-drink_cost, 2)
        print(f"Here is ${ch} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry! That's not enough money")




going_now = True
while(going_now):
    choice = input("Enter your choice espresso/latte/cappuccino: ")
    if (choice == "off"):
        going_now = False
    elif (choice == "report"):
        print(f"Water  : {resources['water']}")
        print(f"Milk   : {resources['milk']}")
        print(f"Coffee : {resources['coffee']}")
    else:
        drink = menu[choice]
        if enough_resources(drink['ingredients']):
            payment = process_coins()
            transaction(payment, drink["cost"])