from coffee_menu import menu
from coffee_menu import resources
profit=0


def check_resource(drink):
    '''checks whether there is sufficient ingredients in machine for drinks '''
    for things in resources:
        if menu[drink]['ingredients'][things]<=resources[things]:
                comp_a = resources[things]
                comp_b=menu[drink]['ingredients'][things]
                remaining = comp_a-comp_b
                resources[things]=remaining
        else:
            print(f"Sorry There is no enough {things}")
            return False
    return True


def check_paisa(drink):
    '''checks whether the amount given by user is sufficient according to drink or not'''
    twenty_five_paisa = int(input("How Many 0.25 paisa u have: ")) *0.25
    fifty_paisa = int(input("How Many 0.50 paisa u have: "))*0.50
    seventy_five_paisa = int(input("How Many 0.75 paisa u have: "))*0.75
    one_rupees= int(input("How Many 1 rupees u have: "))*1.0
    total=round(twenty_five_paisa+fifty_paisa+seventy_five_paisa+one_rupees,2)
    if total==menu[drink]['cost']:
        return True
    elif total>menu[drink]['cost']:
        print(f"Money {total-menu[drink]['cost']} Refunded ")
        return True
    else:
        return False


def mac_on():
    drink = input("What would you like To have (espresso,latte,cappuccino): ").lower()
    if check_resource(drink):
        print(f"Drink Price is {menu[drink]['cost']}")
        print("Insert Coins")
        if check_paisa(drink):
            print(f"Here is You {drink} Enjoy")
            global profit
            profit+=menu[drink]['cost']
            print(f"Money :{profit}")
        else:
            print("Insufficient Money ! Your Money Has been Refunded")


check=True
while check:
    mac_fun= input("Machine is Off Enter 'On' to On the Machine, Enter 'off' to Off the Machine , Enter 'Report' to see the Machine Ingredient: ").lower()
    if mac_fun=='report':
        for thing in resources:
            print(thing,end = ": ")
            print(f"{resources[thing]}g")
        check=True
    elif mac_fun =="on":
        mac_on()
        check=True
    else:
        check=False
