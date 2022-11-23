from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


Money_machine=MoneyMachine()
Coffee_maker=CoffeeMaker()
Menu_of_machine=Menu()
Items=MenuItem

is_on=True

Money_machine.report()
Coffee_maker.report()

while is_on:
    option=Menu_of_machine.get_items()
    choice=input(f"Select the options from menu{option}")
    if choice == 'off':
        is_on=False
    elif choice=='report':
        print(Coffee_Maker.report())
    else:
        drink=Menu_of_machine.find_drink(choice)
        if Coffee_maker.is_resource_sufficient(drink):
            if Money_machine.make_payment(drink.cost):
                Coffee_maker.make_coffee(drink)

