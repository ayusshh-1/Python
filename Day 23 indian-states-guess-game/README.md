🇮🇳 Day 22 - Indian State Guessing Game
This project is a Python-based game using the turtle graphics module where users try to guess all the states of India. Each correct guess places the state name on the map, helping users learn state locations visually.

🗂️ Project Structure

day 22 Indian-State-Game/
├── india_map.gif                  # Background image of India map
├── Indian_States_Coordinates.csv # CSV containing coordinates of states
├── learn_missed_state.csv        # (Auto-generated) List of missed states
└── main.py                       # Main game logic
▶️ How to Play
Run main.py.

A turtle graphics window will appear with the map of India.

Enter the names of Indian states one by one when prompted.

Correct answers appear at their location on the map.

Type Exit to end the game early and save unguessed states in learn_missed_state.csv.

🧠 Objective
Guess all 29 Indian states.

Reinforce memory and learn geographical locations visually.

📊 CSV Format
Indian_States_Coordinates.csv

State,x,y
Maharashtra,-50,120
Kerala,-120,-180
...
🛠️ Developer Tip: Get Map Coordinates
To manually gather coordinates from the map, uncomment the following code in main.py:

# def get_coordinates(x, y):
#     print(x, y)
# screen.onscreenclick(get_coordinates)
# screen.mainloop()
🧾 Requirements
Python 3.x

pandas library (Install via pip install pandas)

Turtle module (comes pre-installed with Python)

✅ Output
State names appear on the map as you guess.

If you type Exit, a learn_missed_state.csv file is created, listing all the states you missed.
