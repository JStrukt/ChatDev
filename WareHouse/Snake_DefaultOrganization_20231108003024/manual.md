# Snake Game

The Snake Game is a classic computer game that originated during the late 1970s. The game requires players to control a line which grows in length, with the line itself being a primary obstacle.

## Quick Install

Before you can run the game, you need to install Python and Pygame. Python is the programming language used to develop this game, and Pygame is a set of Python modules designed for writing video games.

To install Python, visit the official website at https://www.python.org/downloads/ and download the version suitable for your operating system.

To install Pygame, open your terminal or command prompt and type the following command:

```bash
pip install pygame
```

## 🎮 How to Play

The objective of the game is to control the snake and eat as many food items as possible. Each time the snake eats a food item, it grows longer, making the game more challenging. The game ends when the snake collides with the game window border or with its own body.

Here are the controls for the game:

- Use the UP arrow key to move the snake upwards.
- Use the DOWN arrow key to move the snake downwards.
- Use the LEFT arrow key to move the snake to the left.
- Use the RIGHT arrow key to move the snake to the right.

## 📁 File Structure

The game is organized into several Python files, each responsible for a specific aspect of the game:

- `main.py`: This is the main file that runs the game. It initializes the game, handles user inputs, updates the game state, and renders the game on the screen.
- `snake.py`: This file defines the Snake class. It handles the snake's movement, growth, and drawing on the screen.
- `food.py`: This file defines the Food class. It handles the food's spawning and drawing on the screen.
- `grid.py`: This file defines the Grid class. It handles the drawing of the grid on the screen.
- `score.py`: This file defines the Score class. It handles the scoring system of the game.

## 🏁 Starting the Game

To start the game, navigate to the directory containing the game files in your terminal or command prompt and type the following command:

```bash
python main.py
```

Enjoy the game!
