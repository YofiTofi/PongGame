from turtle import Turtle
import random

BALL_SHAPE = "circle"
BALL_COLOR = "white"
BALL_STEP_SIZE = 5
BALL_SPEED = 1

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(BALL_SPEED)
        self.penup()
        self.color(BALL_COLOR)
        self.shape(BALL_SHAPE)
        self.setheading(random.randint(0,1) * 180)
    def move(self):
        if self.is_touching_wall() is not None:
            self.wall_bounce(self.is_touching_wall())
        self.forward(BALL_STEP_SIZE)

    def is_touching_wall(self):
        if self.ycor() > 340:
            return "upper"
        if self.ycor() < -340:
            return "lower"
        return None

    def wall_bounce(self, wall_side):
        if 90 < self.heading() < 270:
            if wall_side == "upper":
                self.setheading(self.heading() + 90 + random.randint(0, 3))
            elif wall_side == "lower":
                self.setheading(self.heading() - 90 + random.randint(0, 3))
        elif self.heading() < 90 or self.heading() > 270:
            if wall_side == "upper":
                self.setheading(self.heading() - 90 + random.randint(0, 3))
            elif wall_side == "lower":
                self.setheading(self.heading() + 90 + random.randint(0, 3))

    def paddle_bounce(self):
        self.setheading(self.heading() - 180 + random.randint(-10, 10))

    def is_out_of_bounds(self):
        if self.xcor() > 500:
            return "right"
        elif self.xcor() < -500:
            return "left"
        return "none"

    def reset_game(self):
        self.goto(0, 0)
        self.setheading(random.randint(0, 360))
