logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
def encrypt(msg,shift):
    print("The encoded Text is ",end="")
    for char in msg:
        if ord(char) in range(97,122):
            ascii_encode=(ord(char)-97+shift)%26 +97
            print(chr(ascii_encode),end="" )
        else:
            print(char,end="")
def decrypt(msg,shift):
    print("The decoded Text is ",end="")
    for char in msg:
        if ord(char) in range(97,122):
            ascii_encode=(ord(char)-97-shift)%26 +97
            print(chr(ascii_encode),end="" )
        else:
            print(char,end="")
while True:
    print("\nEnter 'encrypt' to encrypt the data and for decrypt enter the 'decrypt' and 'break' to stop") 
    a = input().lower()
    if a=="encrypt":
        print("enter the message")
        msg = input()
        print("enter the number of shift")
        shift = int(input())
        encrypt(msg,shift)
    elif a=="decrypt":
        print("enter the message")
        msg = input()
        print("enter the number of shift")
        shift = int(input())
        decrypt(msg,shift)
    elif a=="break":
        print("Good Bye")
        exit()
    else:
        print("You entered a wrong Word ")