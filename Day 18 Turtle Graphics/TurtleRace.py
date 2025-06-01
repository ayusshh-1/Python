from turtle import Turtle ,Screen
screen= Screen()
import random
screen.setup(500,400)
color = ["red","orange","green","blue","purple","yellow"]
x=-230
y_pos=[25,50,75,-25,-50,0]
check = True
all_turtle = []
user_input = screen.textinput(title = "Winner", prompt ="Choose the color of the turtle which will win")
for turtle_index in range(0,6):
    turtle = Turtle(shape="turtle")
    turtle.color(color[turtle_index])
    turtle.penup()
    turtle.goto(x,y_pos[turtle_index])
    all_turtle.append(turtle)
while check:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            check=False
            if user_input == turtle.pencolor():
                print(turtle.pencolor())
                print(f"You Win! {turtle.pencolor()} is Winner")
            else:
                print(f"You lose! {turtle.pencolor()} is Winner")
        turtle.forward(random.randint(0,10))
screen.exitonclick()
