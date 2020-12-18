# ---IMPORTS---
from turtle import Turtle
from config import *


# ---CONSTANTS---

# ---CLASSES---
class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color(PADDLE_COLOR)
        self.shape(PADDLE_SHAPE)
        self.penup()
        self.speed(PADDLE_SPEED)
        self.goto(x_pos, y_pos)
        self.resizemode(PADDLE_RESIZE_MODE)
        self.shapesize(stretch_wid=PADDLE_HEIGHT, stretch_len=PADDLE_WIDTH)

    def moveUp(self):
        new_x = self.xcor()
        new_y = self.ycor() + PADDLE_MOVE_DISTANCE
        self.goto(new_x, new_y)

    def moveDown(self):
        new_x = self.xcor()
        new_y = self.ycor() - PADDLE_MOVE_DISTANCE
        self.goto(new_x, new_y)
