from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(x, y)

    def move_up(self):
        new_y = self.ycor()+10
        self.goto(self.xcor(), new_y)
    def move_down(self):
        new_y = self.ycor()-10
        self.goto(self.xcor(), new_y)