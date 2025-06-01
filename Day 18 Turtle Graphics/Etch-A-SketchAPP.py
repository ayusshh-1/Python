from turtle import Turtle ,Screen
tim = Turtle()
screen = Screen()
x=45
tim.write("Hello")
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def clear_all():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
def clock_wise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def counter_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
screen.listen()
screen.onkey(key="m" ,fun=move_forward)
screen.onkey(key="b" ,fun=move_backward)
screen.onkey(key="c" ,fun=clear_all)
screen.onkey(key="l" ,fun=clock_wise)
screen.onkey(key="r", fun=counter_clockwise)
screen.exitonclick()
