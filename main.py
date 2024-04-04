from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Print a report of all resources
# Creating objects from the classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

# create a report with money machine and coffee maker
money_machine.report() 
coffee_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_resources = coffee_maker.is_resource_sufficient(drink)
        make_payment = money_machine.make_payment(drink.cost)
        if is_enough_resources and make_payment:
            coffee_maker.make_coffee(drink)
            