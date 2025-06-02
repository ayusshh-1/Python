from turtle import Turtle
class Score(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x,y)
        self.write("{}".format(self.lscore), move=False, align='center', font=('Arial', 20, 'bold'))
        self.write("{}".format(self.rscore), move=False, align='center', font=('Arial', 20, 'bold'))
    def l_increase_score(self):
        self.clear()
        self.lscore += 1
        self.write("{}".format(self.lscore), move=False, align='center', font=('Arial', 20, 'bold'))

    def r_increase_score(self):
        self.clear()
        self.rscore += 1
        self.write("{}".format(self.rscore), move=False, align='center', font=('Arial', 20, 'bold'))