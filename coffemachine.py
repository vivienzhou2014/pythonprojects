MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}

money = 0


def cashier(order):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    money_received = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if money_received >= MENU[f"{order}"]["cost"]:
        change = round(money_received - MENU[f"{order}"]["cost"], 2)
        print(
            f"Here is ${change} in change.\nHere is your {order} ☕. Enjoy!")
        global money
        money += MENU[f"{order}"]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")


def check_resources(order, resource):
    resource_needed = MENU[f"{order}"]["ingredients"][f"{resource}"]
    if resources[resource] < resource_needed:
        print(f"Sorry there is not enough {resource}.")
    else:
        resources[resource] -= resource_needed


is_on = True
while is_on:
    order = input("What would you like?(espresso/latte/cappuccino): ")
    if order == "report":
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        print(
            f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}ml\nMoney: ${money}")
    elif order == "off":
        is_on = False
    elif order == "latte" or order == "cappuccino":
        for n in resources:
            check_resources(order, n)
        cashier(order)
    else:
        check_resources(order, "water")
        check_resources(order, "coffee")
        cashier(order)
