from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.ball_speed  = 0.1
    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor()+ self.y_move
        self.goto(x_cor, y_cor)
    def collision_wall(self):
        self.y_move *=-1
    def collision_paddle(self):
        self.x_move *= -1
        self.ball_speed *= 0.9
    def reset_ball(self):
        self.goto(0, 0)
        self.collision_paddle()
        self.ball_speed =0.1


