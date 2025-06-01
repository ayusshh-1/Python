import os

def clear_screen():
    # Works for Windows and Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')