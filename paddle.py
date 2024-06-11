from turtle import Turtle  # Import the Turtle class from the turtle module

class Paddle(Turtle):

    def __init__(self, position):
        # Initialize the Paddle class inheriting from Turtle
        super().__init__()
        self.shape("square")  # Set the shape of the paddle to a square
        self.color("white")  # Set the color of the paddle to white
        self.speed("fast")  # Set the animation speed to fast
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the shape to create a paddle (5 times taller, 1 time wider)
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(position)  # Move the paddle to the given position

    def up(self):
        # Method to move the paddle up
        new_y = self.ycor() + 20  # Calculate the new y-coordinate by adding 20 units
        self.goto(self.xcor(), new_y)  # Move the paddle to the new y-coordinate, keeping the x-coordinate constant

    def down(self):
        # Method to move the paddle down
        new_y = self.ycor() - 20  # Calculate the new y-coordinate by subtracting 20 units
        self.goto(self.xcor(), new_y)  # Move the paddle to the new y-coordinate, keeping the x-coordinate constant
