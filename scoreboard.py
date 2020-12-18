# ---IMPORTS---
from turtle import Turtle
from config import *


# ---CLASSES---
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(SCOREBOARD_COLOR)
        self.left_score = 0
        self.right_score = 0
        self.speed(SCOREBOARD_SPEED)
        self.writeScores()

    def writeScores(self):
        self.clear()
        for player in ("left", "right"):
            x_dist_to_center = SCOREBOARD_X_DISTANCE_TO_CENTER
            score = self.left_score
            if player != "left":
                x_dist_to_center *= -1
                score = self.right_score

            x_position = self.xcor() - x_dist_to_center
            y_position = SCREEN_HEIGHT / 2 - SCOREBOARD_Y_DISTANCE_TO_TOP
            self.goto(x_position, y_position)
            font_tuple = (
                SCOREBOARD_TEXT_FONT,
                SCOREBOARD_TEXT_SIZE,
                SCOREBOARD_TEXT_STYLE
            )
            self.write(
                arg=score,
                align=SCOREBOARD_TEXT_ALIGN,
                font=font_tuple
            )
