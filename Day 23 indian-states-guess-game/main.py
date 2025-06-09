import pandas as pd
from turtle import Turtle, Screen

tim1 = Turtle()
screen = Screen()
screen.setup(800, 800)

map = "india_map.gif"
screen.addshape(map)
tim1.shape(map)

data = pd.read_csv("Indian_States_Coordinates.csv")
state_list = (data.State).tolist()
guessed_list=[]
while len(guessed_list)<30:
    user_input = (screen.textinput(f"{len(guessed_list)}/29 State Correct", "Enter the 'State' Name")).title()  # user input
    if user_input=="Exit":
        missed_state = []
        for name in state_list:
            if name not in guessed_list:
                missed_state.append(name)
        missed_state_csv = pd.DataFrame(missed_state)
        missed_state_csv.to_csv("learn_missed_state.csv")
        break
    if user_input in state_list and user_input not in guessed_list:
        guessed_list.append(user_input)
        tim2 = Turtle()
        tim2.penup()
        tim2.hideturtle()
        state_data = data[data.State == user_input]
        tim2.goto(int(state_data.x), int(state_data.y))
        tim2.write(user_input)


##----------------------------------------- To get The Coordinates ---------------------------------------------
# def get_coordinates(x,y):
#    print(x,y)
# screen.onscreenclick(get_coordinates)
# screen.mainloop()
##----------------------------------------------------------------------------------------------------------------

