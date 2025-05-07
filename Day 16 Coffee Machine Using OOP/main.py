from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker= CoffeeMaker()
money_machine= MoneyMachine()
menu = Menu()
check=True
while check:
    in_put = input(f"What would you like to have {menu.get_items()}? ")
    if in_put=="report":
        money_machine.report()
        coffee_maker.report()
    elif in_put=="off":
        check=False
    else:
        drink=menu.find_drink(in_put)
        if coffee_maker.is_resource_sufficient(drink):
            print(f"drink cost: {drink.cost}")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



