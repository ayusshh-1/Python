import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score=Scoreboard()
car_manager=CarManager()

screen.listen()
screen.onkey(player.turtle_move,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.move_car()
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    #detect the collision with car block
    for car in car_manager.cars:
        if car.distance(player)<20:
            score.game_over()
            game_is_on = False

    #successfully reaching the end point
    if player.at_finish_line():
        score.inc_level()
        player.reset_position()
        car_manager.inc_car_speed()

screen.exitonclick()
