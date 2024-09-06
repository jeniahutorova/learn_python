MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 1.5,
    },
    'capuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    },
}
resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money' : 0
}

machine_off = False

#Check sufficient resources
def check_resources(order):
    for item in MENU[order]['ingredients']:
        if MENU[order]['ingredients'][item] > resources[item]:
            print(f"Sorry, there's not enough {item}.")
            return False
    return True

#Proceed coins
def proceed_money(cost):
    total = 0
    print("Please insert coins.")
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    if total >= cost:
        change = round(total - cost, 2) 
        resources["money"] += cost
        if change > 0 :
            print(f"This is your change: £{change}")
        return True
    else:
        print(f"Sorry it's not enough! This is your refund £{total}.")
        return False

# Make the coffee
def make_coffee(order):
    for item in MENU[order]["ingredients"]:
        resources[item] -= MENU[order]["ingredients"][item]
    print(f"Here is your {order} ☕! Enjoy!")

# Main loop
while not machine_off:
    
    #Prompt user
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    #Turn off the Coffee Machine by entering “off” to the prompt.
    if order == 'off':
        machine_off = True
    
    # Print report of resources
    elif order == 'report':
        print(f"Water : {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {resources['money']}£")

    # Process valid orders
    elif order in MENU:
        drink = MENU[order]
        if check_resources(order):
            if proceed_money(drink["cost"]):
                make_coffee(order)
    
    # Handle invalid input
    else:
        print("Invalid input. Please choose a valid drink (espresso/latte/cappuccino), 'report', or 'off'.")