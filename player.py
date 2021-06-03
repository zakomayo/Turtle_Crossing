
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.original_position()        # user method
        self.shape("turtle")
        self.setheading(90)


    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def original_position(self):
        self.goto(STARTING_POSITION)
