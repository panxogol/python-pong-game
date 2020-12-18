from turtle import Screen
from config import *
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard


# TODO 1: Found all the classes that the game need
def main():
    # 1: Screen
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_BACKGROUND_COLOR)
    screen.tracer(0)

    # 2: Paddles
    r_paddle_x_pos = SCREEN_WIDTH / 2 - PADDLE_DISTANCE_TO_WALL
    r_paddle_y_pos = PADDLE_Y_POSITION
    r_paddle = Paddle(r_paddle_x_pos, r_paddle_y_pos)

    l_paddle_x_pos = -r_paddle_x_pos
    l_paddle_y_pos = PADDLE_Y_POSITION
    l_paddle = Paddle(l_paddle_x_pos, l_paddle_y_pos)

    # TODO 2: Change the keys to config constants
    # Listen to keys up and Down and move the paddle
    screen.listen()
    screen.onkeypress(r_paddle.moveUp, RIGHT_PADDLE_UP_KEY)
    screen.onkeypress(r_paddle.moveDown, RIGHT_PADDLE_DOWN_KEY)
    screen.onkeypress(l_paddle.moveUp, LEFT_PADDLE_UP_KEY)
    screen.onkeypress(l_paddle.moveDown, LEFT_PADDLE_DOWN_KEY)

    # 3. Ball
    ball = Ball()
    # 4: Score
    scoreboard = ScoreBoard()
    game_is_on = True
    while game_is_on:
        screen.update()
        sleep(SCREEN_REFRESH_TIME)
        ball.move(left_paddle=l_paddle, right_paddle=r_paddle, scoreboard=scoreboard)


    # Leave windows only on click
    screen.exitonclick()


if __name__ == "__main__":
    main()
