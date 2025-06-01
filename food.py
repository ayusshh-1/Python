from turtle import Turtle
from Snake import Snake
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        x_cor = random.randint(-280,280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 270)
        self.goto(x_cor, y_cor)