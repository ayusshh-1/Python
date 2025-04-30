import os

def clear_screen():
    # Works for Windows and Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to Blind Auction")
highest_bid=0
person_dict = {}
check_in=True
while check_in:
    name = input("Enter Your Name : ")
    bid = int(input("Enter Your Bid : ₹"))
    person_dict[name] = bid
    lets_check=input("is there any other bidder type yes or no :").lower()
    if lets_check=="yes":
        check_in=True
        clear_screen()
    else:
        check_in=False
for person in person_dict:
    bided = person_dict[person]
    if bided > highest_bid:
        highest_bid=bided
        winner=person
print(f"Highest bidder is {winner} of ₹{highest_bid} ")

