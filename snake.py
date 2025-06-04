from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    """Class to represent the snake in the classic Snake game."""

    def __init__(self):
        """Initialize the snake with default segments and set the head."""
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        """Create the initial snake body using predefined starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Add a new segment to the snake at the specified position.

        Args:
            position (tuple): (x, y) coordinates where the new segment should appear.
        """
        new_turtle = Turtle(shape="square")
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(position)
        self.segment.append(new_turtle)

    def reset_snake(self):
        for seg in self.segment:
            seg.goto((1000, 1000))
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def extend_segment(self):
        """
        Extend the snake by adding a new segment at the last segment's current position.
        This gives the illusion of growth after eating food.
        """
        self.add_segment(self.segment[-1].position())

    def move(self):
        """
        Move the snake forward by having each segment follow the one in front of it.
        The head moves in its current heading direction.
        """
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Change the snake's direction to up, unless it's currently heading down."""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """Change the snake's direction to down, unless it's currently heading up."""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        """Change the snake's direction to right, unless it's currently heading left."""
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        """Change the snake's direction to left, unless it's currently heading right."""
        if self.head.heading() != 0:
            self.head.setheading(180)


