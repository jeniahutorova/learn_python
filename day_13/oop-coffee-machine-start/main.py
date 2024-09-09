from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while is_on:
    #Prompt user
    options = menu.get_items()
    order = input(f"What would you like? ({options}): ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
            coffee_maker.report()
            money_machine.report()
    else:
        drink = menu.find_drink(order)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else:
            print("Sorry, that drink is not available!")