from turtle import Screen
from Snake import Snake
from food import Food
from scroreboard import Score
import time
screen=Screen()
food = Food()
score = Score()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
cord=0
snake = Snake() #this will only create a snake
screen.listen()
check_Flag = True
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
while check_Flag:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detection collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        score.update_score()
        snake.add_snake()
    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        check_Flag = False
        score.game_over()
    #detect collision with itself
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            check_Flag = False
            score.game_over()
screen.exitonclick()
