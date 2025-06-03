from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.write("level:{}".format(self.level), align="left", font=FONT)

    def inc_level(self):
        self.clear()
        self.level+=1
        self.write("level:{}".format(self.level), align="left", font=FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write("Game Over".format(self.level), align="center", font=FONT)

