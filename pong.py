from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import winsound


def draw_center_line():
    # Function to draw the center dashed line on the screen
    line = Turtle()
    line.color("white")
    line.penup()
    line.goto(0, 300)
    line.setheading(270)
    line.hideturtle()
    line.width(2)
    for _ in range(15):
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(20)


def screen_setup(scn, pdl_1, pdl_2):
    # Function to set up the screen and key bindings
    scn.bgcolor("black")
    scn.setup(width=800, height=600)
    scn.title("Pong")
    scn.tracer(0)
    scn.listen()
    scn.onkey(pdl_1.up, "Up")
    scn.onkey(pdl_1.down, "Down")
    scn.onkey(pdl_2.up, "w")
    scn.onkey(pdl_2.down, "s")


def display_game_over(winner):
    # Function to display the game over message
    game_over = Turtle()
    game_over.color("white")
    game_over.penup()
    game_over.hideturtle()
    winsound.PlaySound("SystemExit", winsound.SND_ASYNC)
    game_over.write(f"Game Over! {winner} wins!", align="center", font=("Courier", 24, "normal"))
    time.sleep(2)
    game_over.clear()


def countdown_timer():
    countdown = Turtle()
    countdown.color("white")
    countdown.penup()
    countdown.hideturtle()
    countdown.goto(0, 0)
    for i in range(3, 0, -1):
        countdown.write(i, align="center", font=("Courier", 48, "normal"))
        time.sleep(1)
        countdown.clear()
    countdown.write("Go!", align="center", font=("Courier", 48, "normal"))
    time.sleep(1)
    countdown.clear()


def reset_game(r_ple, l_ple, bll, sboard):
    r_ple.goto(350, 0)
    l_ple.goto(-350, 0)
    bll.reset_position()
    sboard.reset_scores()
    countdown_timer()


if __name__ == '__main__':
    # Main script execution starts here
    screen = Screen()  # Initialize the screen
    winning_score = screen.numinput("Winning Score", "Enter the winning score: ", minval=1, maxval=20)
    r_paddle = Paddle((350, 0))  # Create the right paddle
    l_paddle = Paddle((-350, 0))  # Create the left paddle
    ball = Ball()  # Create the ball
    scoreboard = Scoreboard()  # Create the scoreboard
    draw_center_line()  # Draw the center line
    screen_setup(screen, r_paddle, l_paddle)  # Set up the screen and key bindings
    countdown_timer()  # Initial countdown before the game starts

    game_is_on = True  # Game loop control variable
    while game_is_on:
        time.sleep(ball.move_speed)  # Control the ball's speed
        screen.update()  # Update the screen
        ball.move()  # Move the ball

        # Detect collision with wall and bounce the ball
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddles and bounce the ball
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        # Detect right paddle misses and reset ball position
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()  # Award a point to the left player

        # Detect left paddle misses and reset ball position
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()  # Award a point to the right player

        # Check if a player wins
        if scoreboard.l_score == winning_score:
            game_is_on = False
            display_game_over("Player 1")  # Display game over message for player 1
            reset_game(r_paddle, l_paddle, ball, scoreboard)  # Reset the game
            game_is_on = True  # Restart the game

        if scoreboard.r_score == winning_score:
            game_is_on = False
            display_game_over("Player 2")  # Display game over message for player 2
            reset_game(r_paddle, l_paddle, ball, scoreboard)  # Reset the game
            game_is_on = True  # Restart the game

    screen.exitonclick()  # Exit the game on click
