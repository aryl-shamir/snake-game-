from turtle import Turtle

class Scoreboard(Turtle):
    """
    A class to manage the scoreboard for the Snake game.
    Inherits from the Turtle class to display the score on the screen.
    """

    def __init__(self):
        """
        Initializes the scoreboard by setting position, appearance, and starting score.
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto((0, 280))  # Position at top center of the screen
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the scoreboard display with the current score.
        """
        self.write(f"Score = {self.score}", False, align="center")

    def game_over(self):
        """
        Displays the 'Game Over' message at the center of the screen.
        """
        self.goto((0, 0))
        self.write("Game Over", False, align="center")

    def increase_score(self):
        """
        Increases the score by one and updates the scoreboard display.
        Clears the previous score to avoid overlap.
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()
