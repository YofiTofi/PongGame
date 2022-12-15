from gameboard import Gameboard
from turtle import Screen
from paddle import Paddle
import time

SCREEN_TITLE = "Pong Game"
SCREEN_COLOR = "black"
SCREEN_SIZE = ()
screen = Screen()
screen.tracer(0)
screen.title(SCREEN_TITLE)
screen.bgcolor(SCREEN_COLOR)
screen.setup(width=1000, height=700)
gameboard = Gameboard()

lpaddle = Paddle(paddle_side="left")
rpaddle = Paddle(paddle_side="right")
screen.update()
game_on = True
screen.listen()
while game_on:
    screen.update()
    screen.onkeypress(key="w", fun=lpaddle.move_up)
    screen.onkeypress(key="s", fun=lpaddle.move_down)
    screen.onkeypress(key="Up", fun=rpaddle.move_up)
    screen.onkeypress(key="Down", fun=rpaddle.move_down)
    screen.update()
screen.exitonclick()
screen.mainloop()