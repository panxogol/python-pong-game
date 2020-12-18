# ---IMPORTS---
from turtle import Turtle
from config import *


# ---CLASSES---
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(BALL_COLOR)
        self.speed(BALL_TURTLE_SPEED)
        self.shape(BALL_SHAPE)
        self.width(BALL_WIDTH)
        self.penup()
        self.move_speed = BALL_MOVEMENT_SPACE
        self.x_move = self.move_speed
        self.y_move = -self.move_speed

    def move(self, left_paddle: Turtle, right_paddle: Turtle, scoreboard):
        self.bounce(left_paddle, right_paddle)
        self.resetWhenLeave(score_board=scoreboard)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, l_paddle: Turtle, r_paddle: Turtle):
        # Bounce with top and bottom walls
        y_limit = (SCREEN_HEIGHT - self.width()) / 2
        if self.ycor() >= y_limit or self.ycor() <= -y_limit:
            self.y_move *= -1

        # Bounce with left and right paddles
        x_limit = SCREEN_WIDTH / 2 - PADDLE_DISTANCE_TO_WALL - BALL_BOUNCING_X_ERROR_SPACE
        distance_to_l_paddle = self.distance(l_paddle)
        distance_to_r_paddle = self.distance(r_paddle)
        has_touched_paddle = (
                (self.xcor() <= -x_limit or self.xcor() >= x_limit) and
                (distance_to_r_paddle <= BALL_BOUNCING_DISTANCE_TO_PADDLE
                 or distance_to_l_paddle <= BALL_BOUNCING_DISTANCE_TO_PADDLE)
        )
        if has_touched_paddle:
            self.x_move *= -(1 + BALL_INCREASE_SPEED_WHEN_TOUCH_PADDLE)
            self.y_move *= 1 + BALL_INCREASE_SPEED_WHEN_TOUCH_PADDLE

    def resetWhenLeave(self, score_board):
        limit = SCREEN_WIDTH / 2
        x_value = self.xcor()
        if x_value > limit or x_value < -limit:
            if x_value > limit:
                score_board.left_score += 1
            elif x_value < -limit:
                score_board.right_score += 1
            score_board.writeScores()
            self.home()
            self.x_move = (self.x_move / abs(self.x_move)) * -self.move_speed
            self.y_move = (self.y_move / abs(self.y_move)) * self.move_speed
