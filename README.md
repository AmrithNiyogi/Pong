# Pong

This is a Python implementation of the classic Pong game using the Turtle graphics library. 

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

The game allows two players to control paddles to bounce a ball back and forth, scoring points when the opposing player misses the ball. The game includes sound effects, a customizable winning score, and a countdown timer before the game starts.

## Features

- Two-player gameplay with separate controls for each paddle.
- Sound effects for ball collisions.
- Customizable winning score.
- Countdown timer before the game starts.
- Center dashed line and border for visual appeal.
- Reset functionality to restart the game after it ends.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/AmrithNiyogi/pong.git
    ```

2. Navigate to the project directory:
    ```sh
    cd pong
    ```

3. Ensure you have Python installed (preferably version 3.6 or above).

4. Install the required dependencies (if any):
    ```sh
    pip install winsound
    ```

## Usage

To start the game, run the following command:
```sh
python pong.py
```

## Controls

- Player 1 (Left Paddle): Up (W key), Down (S key)
- Player 2 (Right Paddle): Up (Up Arrow), Down (Down Arrow)

## Code Structure

- `pong.py`: The entry point for the game. Sets up the screen and starts the game loop.
- `paddle.py`: Contains the `Paddle` class for paddle movement.
- `ball.py`: Contains the `Ball` class for ball movement and collision detection.
- `scoreboard.py`: Contains the `Scoreboard` class which manages the score display and game over message.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
   
