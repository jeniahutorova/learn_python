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

mashine_off = False
def check_resources():
    for item in MENU['ingridients']:
        if MENU[order]['ingredients'][item] > resources[item]:
            print(f"Sorry, there's not enough {item}.")
            return False
        return True

while not mashine_off:
    #Prompt user
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    #Turn off the Coffee Machine by entering “off” to the prompt.
    if order == 'off':
        mashine_off = True
    elif order == 'report':
        print(resources)
    elif order in MENU:
        
