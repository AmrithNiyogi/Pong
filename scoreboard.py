from turtle import Turtle  # Import the Turtle class from the turtle module

class Scoreboard(Turtle):
    def __init__(self):
        # Initialize the Scoreboard class inheriting from Turtle
        super().__init__()
        self.color("white")  # Set the text color to white
        self.penup()  # Lift the pen to avoid drawing lines
        self.hideturtle()  # Hide the turtle icon (only show text)
        self.l_score = 0  # Initialize the left player's score to 0
        self.r_score = 0  # Initialize the right player's score to 0
        self.update_scoreboard()  # Update the scoreboard with initial scores

    def update_scoreboard(self):
        # Function to update the scoreboard display
        self.clear()  # Clear the previous scoreboard
        self.goto(-200, 250)  # Move to position for Player 1 label
        self.write("Player 1", align="center", font=("Courier", 20, "normal"))  # Display Player 1 label
        self.goto(-100, 220)  # Move to position for Player 1 score
        self.write(self.l_score, align="center", font=("Courier", 60, "bold"))  # Display Player 1 score
        self.goto(200, 250)  # Move to position for Player 2 label
        self.write("Player 2", align="center", font=("Courier", 20, "normal"))  # Display Player 2 label
        self.goto(100, 220)  # Move to position for Player 2 score
        self.write(self.r_score, align="center", font=("Courier", 60, "bold"))  # Display Player 2 score

    def l_point(self):
        # Function to increase the left player's score by 1
        self.l_score += 1
        self.update_scoreboard()  # Update the scoreboard with new scores

    def r_point(self):
        # Function to increase the right player's score by 1
        self.r_score += 1
        self.update_scoreboard()  # Update the scoreboard with new scores

    def reset_scores(self):
        # Function to reset both players' scores to
        # Function to reset both players' scores to 0
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()  # Update the scoreboard with reset scores
