from turtle import Turtle


PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"
PADDLE_SIZE = 4
PADDLE_STEP_SIZE = 15
PADDLE_X_MARGIN = 30
PADDLE_VERTICAL_MARGIN = PADDLE_SIZE * 20


class Paddle:

    def __init__(self, paddle_side):
        self.body = []
        for _ in range(PADDLE_SIZE):
            self.body.append(Turtle(shape=PADDLE_SHAPE))
            self.body[_].color(PADDLE_COLOR)
            self.body[_].penup()
            if paddle_side == "left":
                self.body[_].goto(-500 + PADDLE_X_MARGIN, 0 + 20 * _)
            elif paddle_side == "right":
                self.body[_].goto(500 - PADDLE_X_MARGIN, 0 + 20 * _)

    def move_down(self):
        bottom_cor = self.body[PADDLE_SIZE - 1].ycor()
        for _ in self.body:
            if bottom_cor > -350 + PADDLE_VERTICAL_MARGIN:
                _.setheading(270)
                _.forward(PADDLE_STEP_SIZE)

    def move_up(self):
        top_cor = self.body[0].ycor()
        for _ in self.body:
            if top_cor < 350 - PADDLE_VERTICAL_MARGIN:
                _.setheading(90)
                _.forward(PADDLE_STEP_SIZE)
