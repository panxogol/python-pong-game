from turtle import Screen
from config import *
from paddle import Paddle

# TODO 1: Found all the classes that the game need
# 1: Screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BACKGROUND_COLOR)

# 2: Paddles
r_paddle_x_pos = SCREEN_WIDTH / 2 - PADDLE_DISTANCE_TO_WALL
r_paddle_y_pos = PADDLE_Y_POSITION
r_paddle = Paddle(r_paddle_x_pos, r_paddle_y_pos)

l_paddle_x_pos = -r_paddle_x_pos
l_paddle_y_pos = PADDLE_Y_POSITION
l_paddle = Paddle(l_paddle_x_pos, l_paddle_y_pos)

# Listen to keys up and Down and move the paddle
screen.listen()
screen.onkeypress(r_paddle.moveUp, "Up")
screen.onkeypress(r_paddle.moveDown, "Down")
screen.onkeypress(l_paddle.moveUp, "w")
screen.onkeypress(l_paddle.moveDown, "s")

# 3. Ball
# 4: Score

if __name__ == "__main__":
    screen.exitonclick()