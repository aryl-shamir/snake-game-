from turtle import Turtle
import random

class Food(Turtle):
    """
    A class to represent the food in the Snake game.
    Inherits from the Turtle class and represents the object the snake eats to grow.
    """

    def __init__(self):
        """
        Initializes the food object with shape, color, and random position on the screen.
        The food is made small and placed randomly within the screen bounds.
        """
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()  # Prevents the food from drawing lines as it moves
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Make the food smaller
        self.refresh()  # Position the food randomly on the screen

    def refresh(self):
        """
        Moves the food to a new random location within the screen bounds.
        This is called whenever the snake eats the food.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
