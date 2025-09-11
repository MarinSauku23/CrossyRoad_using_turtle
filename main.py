from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.tracer(0)

screen.listen()
screen.onkey(player.move,"Up")

t = 0.1
loop_run = 0
game_is_on = True
while game_is_on:
    time.sleep(t)
    screen.update()

    if player.ycor() == 280:
        player.reset()
        car_manager.increase_speed()
        score_board.increase_score()

    if loop_run % 6 == 0:
        car_manager.create_car()
    car_manager.move_car()
    loop_run += 1

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()


screen.exitonclick()