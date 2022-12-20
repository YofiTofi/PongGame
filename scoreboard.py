from turtle import Turtle
SCORE_COLOR = "white"
SCORE_Y_OFFSET = 10
SCORE_X_OFFSET = 10



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color(SCORE_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.left = 0
        self.right = 0
        self.write(f"{self.left}  |  {self.right}", move=False, align="center", font=("Lucida Console", 25, "bold"))

    def append_score(self, side):
        matcher = {"right": 0, "left": 1}
        self.__setattr__(side, self.__getattribute__(side) + 1)
        self.clear()
        self.write(f"{self.left}  |  {self.right}", move=False, align="center", font=("Lucida Console", 25, "bold"))

