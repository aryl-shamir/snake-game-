# ---- Import libraries ----
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# ---- Set up screen ----
screen = Screen()
screen.tracer(0)  # Turn off automatic screen updates for smoother animation
screen.listen()
screen.title("Welcome to the Snake Game.")
screen.setup(width=600, height=600)
screen.bgcolor("black")

# ---- Set up constants ----
COLLISION_DISTANCE = 15  # Distance threshold for collision detection
WALL_LIMIT = 290         # Wall boundary coordinates

# ---- Initialize game objects ----
serpent = Snake()
food = Food()
scoreboard = Scoreboard()

# ---- Define key bindings for snake movement ----
screen.onkey(serpent.up, 'Up')
screen.onkey(serpent.down, 'Down')
screen.onkey(serpent.right, 'Right')
screen.onkey(serpent.left, 'Left')

# ---- Start the game loop ----
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    serpent.move()

    # ---- Detect collision with food ----
    if serpent.head.distance(food) < COLLISION_DISTANCE:
        food.refresh()
        scoreboard.increase_score()
        serpent.extend_segment()

    # ---- Detect collision with wall ----
    if (
        serpent.head.xcor() > WALL_LIMIT or
        serpent.head.xcor() < -WALL_LIMIT or
        serpent.head.ycor() > WALL_LIMIT or
        serpent.head.ycor() < -WALL_LIMIT
    ):
        is_game_on = False
        scoreboard.game_over()

    # ---- Detect collision with tail ----
    for segment in serpent.segment[1:]:  # Exclude the head from checking
        if serpent.head.distance(segment) < COLLISION_DISTANCE:
            is_game_on = False
            scoreboard.game_over()

# ---- Wait for user to click before closing the window ----
screen.exitonclick()
