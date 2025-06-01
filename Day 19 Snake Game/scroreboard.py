from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write("Score:{}".format(self.score), move=False, align='center', font=('Arial', 20, 'bold'))

    def update_score(self):
        self.clear()
        self.score+=1
        self.write("Score:{}".format(self.score), move=False, align='center', font=('Arial', 20, 'bold'))
    def game_over(self):
        self.clear()
        self.write("Game over Your Score:{}".format(self.score), move=False, align='center', font=('Arial', 20, 'bold'))
