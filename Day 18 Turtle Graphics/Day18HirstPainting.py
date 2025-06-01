import colorgram,random
rgb_color=[]
colors = colorgram.extract('image.jpg',30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color=(r,g,b)
    rgb_color.append(new_color)
print(rgb_color)
from turtle import Turtle,Screen,colormode
colormode(255)
turtle = Turtle()
def draw_in():
    for _ in range(10):
        turtle.dot(20,random.choice(rgb_color))
        turtle.penup()
        turtle.forward(50)
for i in range(-200,300,50):
    turtle.teleport(-200,i)
    turtle.width(25)
    draw_in()
turtle.hideturtle()
screen = Screen()
screen.exitonclick()