from turtle import Turtle,Screen
import time
cord=0
class Snake:
    def __init__(self):
        self.snake=[]
        self.snake_m()
        self.head = self.snake[0]
    def snake_m(self):
        for i in range(0, 60, 20):
            tim = Turtle(shape='square')
            tim.color('white')
            tim.penup()
            tim.setposition(cord - i, 0)
            self.snake.append(tim)
    def move(self):
        for i in range(len(self.snake)-1,0,-1):
                print(i)
                x_cor = self.snake[i-1].xcor()
                y_cor = self.snake[i-1].ycor()
                self.snake[i].setposition(x_cor,y_cor)
        self.head.forward(20)
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

    def add_snake(self):
        tim1 = Turtle(shape='square')
        tim2 = self.snake[len(self.snake)-1]
        self.snake.append(tim1)
        tim1.color('white')
        tim1.penup()
        tim1.goto(tim2.xcor(), tim2.ycor())

    def reset_snake(self):
        for snake in self.snake:
            snake.goto(1000,1000)
        self.snake.clear()
        self.snake_m()
        self.head = self.snake[0]



