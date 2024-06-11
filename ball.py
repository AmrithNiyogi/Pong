from turtle import Turtle
import winsound  # Library to play sound effects

def play_sound():
    # Function to play a sound asynchronously when the ball bounces
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

class Ball(Turtle):

    def __init__(self):
        # Initialize the Ball class inheriting from Turtle
        super().__init__()
        self.color("white")  # Set the initial color of the ball to white
        self.shape("circle")  # Set the shape of the ball to a circle
        self.penup()  # Lift the pen to avoid drawing lines
        self.x_move = 10  # Initial movement in the x direction
        self.y_move = 10  # Initial movement in the y direction
        self.move_speed = 0.1  # Initial speed of the ball

    def move(self):
        # Method to move the ball on the screen
        new_x = self.xcor() + self.x_move  # Calculate new x-coordinate
        new_y = self.ycor() + self.y_move  # Calculate new y-coordinate
        self.goto(new_x, new_y)  # Move the ball to the new coordinates

        # Change the ball color based on the direction of movement
        if self.x_move > 0:
            self.color("blue")  # Color the ball blue if moving right
        else:
            self.color("red")  # Color the ball red if moving left

    def bounce_y(self):
        # Method to bounce the ball off horizontal walls
        self.y_move *= -1  # Reverse the y-direction
        play_sound()  # Play the bounce sound effect

    def bounce_x(self):
        # Method to bounce the ball off paddles
        self.x_move *= -1  # Reverse the x-direction
        self.move_speed *= 0.9  # Increase the speed of the ball by reducing the delay
        play_sound()  # Play the bounce sound effect

    def reset_position(self):
        # Method to reset the ball to the center of the screen
        self.goto(0, 0)  # Move the ball to the center
        self.move_speed = 0.1  # Reset the speed of the ball
        self.bounce_x()  # Bounce the ball to start moving in the opposite x direction
