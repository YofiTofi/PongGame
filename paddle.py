from turtle import Turtle


PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"
PADDLE_SIZE = 5
PADDLE_STEP_SIZE = 15
PADDLE_X_MARGIN = 30
PADDLE_VERTICAL_MARGIN = PADDLE_SIZE * 10


class Paddle(Turtle):

    def __init__(self, paddle_side):
        super().__init__()
        self.color(PADDLE_COLOR)
        self.shape(PADDLE_SHAPE)
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=PADDLE_SIZE)
        self.penup()
        if paddle_side == "right":
            self.goto(500 - PADDLE_X_MARGIN, 0)
        elif paddle_side == "left":
            self.goto( -500 + PADDLE_X_MARGIN, 0)

    def move_down(self):
        if self.ycor() > -350 + PADDLE_VERTICAL_MARGIN:
            self.setheading(270)
            self.forward(PADDLE_STEP_SIZE)

    def move_up(self):
        if self.ycor() < 350 - PADDLE_VERTICAL_MARGIN:
            self.setheading(90)
            self.forward(PADDLE_STEP_SIZE)
