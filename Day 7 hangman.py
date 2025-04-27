names=["ayushh","nitinn","letsgogo","letsfindd","getting"]
logo = ''' _   _                                             
 _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                           
'''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)
lives =6 
empty=[]
import random
rand_num= random.randint(0,4)
choosen_word = names[rand_num]
for i in range(len(choosen_word)):
    empty.append("_")
print(choosen_word)
print(empty)
while "_" in empty:
    guess = input("enter the alphabet: ").lower()

    for position in range(len(choosen_word)):
        letter  = choosen_word[position]
        if letter==guess:
            # print("Right")
            empty[position]=letter
    if guess not in empty:
        print(f"you enter wrong character {guess}")
        print(stages[lives])
        lives-=1
        if lives == -1 :
            print("game over")
            exit()
    print(empty)  
print("you win")