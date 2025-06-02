from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import Score
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)
screen.bgcolor("black")
r_paddle = Paddle(370,0)
l_paddle = Paddle(-370,0)
ball=Ball()
screen.listen()
l_score=Score(-40,260)
r_score=Score(40,260)
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"u")
screen.onkey(l_paddle.move_down,"d")
check_flag=True

while check_flag:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    
    #detect the collision with the up and down wall
    
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.collision_wall()
        
    #detect the collision with right left nd
    
    if (r_paddle.distance(ball)<40 and ball.xcor()>350) or (l_paddle.distance(ball)<40 and ball.xcor()<-350):
       ball.collision_paddle()
        
#right side paddle miss
    
    if ball.xcor()>380:
        l_score.l_increase_score()
        ball.reset_ball()
        
#left side paddle miss
    
    if ball.xcor()<-380:
        r_score.r_increase_score()
        ball.reset_ball()
screen.exitonclick()
