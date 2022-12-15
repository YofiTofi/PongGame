from turtle import Turtle

BALL_SHAPE = "circle"
BALL_COLOR = "white"


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(BALL_COLOR)
        self.shape(BALL_SHAPE)