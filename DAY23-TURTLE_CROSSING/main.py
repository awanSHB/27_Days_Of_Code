from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import Scoreboard
import time

from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

is_game_on = True
while (is_game_on):
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detecting the collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            score_board.game_over()
    
    # Player crosses the finish line, throwing palyer to starting position, increasing the speed of the car
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()

screen.exitonclick()