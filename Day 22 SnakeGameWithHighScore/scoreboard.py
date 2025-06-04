from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score= 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(20,270)
        self.show_score()

    def show_score(self):
        with open("highest_score.txt") as data:
            self.highest_score = int(data.read())
        self.write(f"Score:{self.score} Highest Score :{self.highest_score}", move=False, align='center', font=('Arial', 20, 'bold'))

    def update_score(self):
        self.clear()
        self.score+=1
        self.show_score()
    # def game_over(self):
    #     self.clear()
    #     self.write("Game over Your Score:{}".format(self.score), move=False, align='center', font=('Arial', 20, 'bold'))

    def restart_game(self):
        self.clear()
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score.txt" , "w") as data:
                data.write(str(self.highest_score))
        self.score = 0
        self.show_score()