#from gameboard import Gameboard
from turtle import Screen
from paddle import Paddle
import time
from scoreboard import Scoreboard
from ball import Ball

SCREEN_TITLE = "Pong Game"
SCREEN_COLOR = "black"
SCREEN_SIZE = ()
screen = Screen()
screen.tracer(0)
PADDLE_CONTACT_SENSITIVITY = 50
screen.title(SCREEN_TITLE)
screen.bgcolor(SCREEN_COLOR)
screen.setup(width=1000, height=700)
#gameboard = Gameboard()
score = Scoreboard()
lpaddle = Paddle(paddle_side="left")
rpaddle = Paddle(paddle_side="right")
screen.update()
game_on = True
screen.listen()
ball = Ball()
ball.setheading(60)
while game_on:
    screen.update()
    screen.onkeypress(key="w", fun=lpaddle.move_up)
    screen.onkeypress(key="s", fun=lpaddle.move_down)
    screen.onkeypress(key="Up", fun=rpaddle.move_up)
    screen.onkeypress(key="Down", fun=rpaddle.move_down)
    screen.update()
    if ball.is_out_of_bounds() == "right":
        score.append_score("left")
        ball.reset_game()
    elif ball.is_out_of_bounds() == "left":
        score.append_score("right")
        ball.reset_game()
    if lpaddle.distance(ball.position()) < PADDLE_CONTACT_SENSITIVITY or rpaddle.distance(ball) < PADDLE_CONTACT_SENSITIVITY:
        ball.paddle_bounce()
    time.sleep(0.015)
    ball.move()
screen.exitonclick()
screen.mainloop()