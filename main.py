# Import Libraries
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing!")

player = Player()

car_manager = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

level_counter = 1

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()

    #Detect collision with turtle and cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False

    if player.next_level():
        player.original_position()
        car_manager.speed_increase()
        scoreboard.increase_level()


screen.exitonclick()
