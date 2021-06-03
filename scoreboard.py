
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()        # User-defined method


    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 230)
        self.write(f"Level: {self.level}", font= FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()