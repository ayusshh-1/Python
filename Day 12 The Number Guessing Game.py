print("Welcome to Guess the Number Game")
logo='''
   ____     _   _ U _____ u ____    ____          _____    _   _  U _____ u      _   _       _   _   __  __     ____  U _____ u   ____     
U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u      |_ " _|  |'| |'| \| ___"|/     | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u  
\| |  _ / \| |\| | |  _|" <\___ \/<\___ \/         | |   /| |_| |\ |  _|"      <|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/  
 | |_| |   | |_| | | |___  u___) | u___) |        /| |\  U|  _  |u | |___      U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <    
  \____|  <<\___/  |_____| |____/>>|____/>>      u |_|U   |_| |_|  |_____|      |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\   
  _)(|_  (__) )(   <<   >>  )(  (__))(  (__)     _// \\_  //   \\  <<   >>      ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_  
 (__)__)     (__) (__) (__)(__)    (__)         (__) (__)(_") ("_)(__) (__)     (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__) 
'''
print(logo)
import random
'''------------------------------------------------------------------------------'''
def game_start(rand_num,attempt):
    '''Game Logic starts from here'''
    print("Enter the Number Between 1 and 100")
    print(f"You have {attempt} attempt to guess the number")
    while attempt!=0:
        att_input=int(input("Guess the Number: "))
        if att_input>rand_num:
            print("Too High")
            attempt-=1
            print(f"You have now {attempt} attempts")
            if attempt==0:
                print("Game Over")
        elif att_input<rand_num:
            print("Too Low")
            attempt-=1
            print(f"You have now {attempt} attempts")
            if attempt==0:
                print("Game Over")
        elif att_input==rand_num:
            print("You Got it")
            print("Game Over")
            attempt=0
        else:
            print("You Lose")
            print("Game Over")
'''------------------------------------------------------------------------------------------------'''
level=input("Difficulty level : \nType 'easy' for easy\n'medium' for Medium\n'difficult' for Difficult level\n :").lower()
rand_num=random.randint(1,100)
if level=="easy":
    game_start(rand_num,10)
elif level=="medium":
    game_start(rand_num,7)
else:
    game_start(rand_num,5)