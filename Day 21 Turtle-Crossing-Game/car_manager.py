from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars=[]
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_appearance = random.randint(1,6)
        if random_appearance == 1 or random_appearance == 4:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_len =2,stretch_wid=1)
            car.penup()
            y_cor = random.randint(-250,250)
            car.goto(300,y_cor)
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def inc_car_speed(self):
        self.car_speed += MOVE_INCREMENT

        # MOVE_INCREMENT+=5





