MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
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
    "money": 0
}

def report():
    print("Water: "+str(resources["water"])+"ml")
    print("Milk: "+str(resources["milk"])+"ml")
    print("Coffee: "+str(resources["coffee"])+"gr")
    print("Money: $"+str(resources["money"]))

def check_resources(selected):
    if resources["water"] < MENU[selected]["ingredients"]["water"]:
        print("Sorry, there is no enough water")
        return False
    elif resources["milk"] < MENU[selected]["ingredients"]["milk"]:
        print("Sorry, there is no enough milk")
        return False
    elif resources["coffee"] < MENU[selected]["ingredients"]["coffee"]:
        print("Sorry, there is no enough coffee")
        return False
    return True

def calculate_money(quarter,dimes,nickles,pennies):
    return quarter*0.25+dimes*0.10+nickles*0.05+pennies*0.01

def update_resources(selected):
    resources["water"] -= MENU[selected]["ingredients"]["water"]
    resources["milk"] -= MENU[selected]["ingredients"]["milk"]
    resources["coffee"] -= MENU[selected]["ingredients"]["coffee"]
    resources["money"] += MENU[selected_coffee]["cost"]

while True:
    selected_coffee = input("What would you like? (espresso/latte/cappuccino):").lower()

    if selected_coffee == "off":
        exit()
    elif selected_coffee == "report":
        report()

    elif check_resources(selected_coffee):
        print("Please insert coins.")
        quarter = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = calculate_money(quarter, dimes, nickles, pennies)

        if total > int(MENU[selected_coffee]["cost"]):
            change = round(total-MENU[selected_coffee]["cost"],2)
            print(f"Here is ${change} in change.")
            print(f"Here is your {selected_coffee} ☕. Enjoy!")
            update_resources(selected_coffee)
        else:
            print("Sorry, that's not enough money.Money refunded.")