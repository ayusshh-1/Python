logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
import random
print("Welcome to Blackjack Game")
check=True
check1=True
new_u_value=0
d_total=0
def user_sum(user_cards):
    return sum(user_cards)
def dealer_sum(dealer_cards):
    return sum(dealer_cards)
def dealer_append(dealer_cards):
    d_card_ran = random.choice(cards)
    dealer_cards.append(d_card_ran)
def user_append(user_cards):
    u_card_ran = random.choice(cards)
    if u_card_ran==11 and user_sum(user_cards)>21:
        u_card_ran = 1
    user_cards.append(cards[u_card_ran])
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_card1 = random.choice(cards)                
user_card2 = random.choice(cards)  
if user_card1==11 and user_card2==11:
    user_card2=1
dealer_card1 = random.choice(cards)  
dealer_card2 = random.choice(cards)  
user_cards=[cards[user_card1],cards[user_card2]]
u_total = user_sum(user_cards)
print(f"User {user_cards} total is {u_total}")
dealer_cards = [cards[dealer_card1]]
print(f"Dealer {dealer_cards}")
while check:
    user_input= input("Enter 'y' to hit and 'n' to stay :")
    if user_input=="n":
        dealer_cards.append(dealer_card2)
        d_total = dealer_sum(dealer_cards)
        print(f"Dealer {dealer_cards} total is {d_total}")
        while d_total<=16:
            dealer_append(dealer_cards)
            d_total=dealer_sum(dealer_cards)
            print(f"Dealer {dealer_cards} total is {d_total}")
        u_total = user_sum(user_cards)
        print(f"User {user_cards} total is {u_total}")
        check=False
    if user_input=="y":
        user_append(user_cards)
        u_total=user_sum(user_cards)
        print(f"User {user_cards} total is {u_total}")
        if u_total>21:
            check=False
            check1=False
            print("Dealer Win")
while check1:
    if (u_total%22)>(d_total%22):
        print("User Win")
        check1=False
    elif (u_total%22)<(d_total%22):
        print("Dealer Win")
        check1=False
    else:
        print("Draw")
        check1=False
        
    
    