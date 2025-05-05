from game_data import data
import random
from art import logo
from art import vs
from clear import clear_screen
check=True
check1=False
check2 = True
count=0
while check:
    print(logo)
    if check2:
        comp_a = random.choice(data)
    if check1:
        print(f"You're Right ,Your current Score is {count}")
    print(f" Compare A : {comp_a['name']}, a {comp_a['description']} , from {comp_a['country']}")
    print(vs)
    comp_b = random.choice(data)
    if comp_a==comp_b:
        comp_b = random.choice(data)
    print(f" Against B : {comp_b['name']}, a {comp_b['description']} , from {comp_b['country']}")
    A = comp_a['follower_count']
    B = comp_b['follower_count']
    choose = input("Who has more Follower ? Type 'A' or 'B' ").lower()
    if choose=='a':
        if A>B:
            count+=1
            check = True #iterate again
            check1 = True #Now show the score
            clear_screen() #clear the screen
            check2 = False #dont change A
        else:
            clear_screen()
            print(logo)
            print(f"Sorry Final Score :{count}")
            check = False
    if choose=='b':
        if B>A:
            count+=1
            check = True  #iterate again
            check1 = True  #Now show the score
            clear_screen()  #clear the screen
            comp_a=comp_b   #assign B to A
            check2 = False   #dont change A now
        else:
            clear_screen()
            print(logo)
            print(f"Sorry,that' wrong Final Score :{count}")
            check=False
    else:
        print("You entered Wrong ")
        check = True
