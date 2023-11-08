manual.md

```
# Snake Game

A classic Snake game developed using Python and Pygame. The game involves guiding a snake through a bounded plane, collecting food items, and avoiding collision with the snake's own body and walls.

## Quick Install

Before you can run the game, you need to install the required dependencies. You can do this by running the following command in your terminal:

`pip install -r requirements.txt`

## 🎮 How to Play

The game is controlled using the arrow keys on your keyboard. The snake moves in the direction of the arrow key pressed. The snake cannot stop once it starts moving and cannot reverse direction 180 degrees.

- Use the UP arrow key to move the snake upwards.
- Use the DOWN arrow key to move the snake downwards.
- Use the LEFT arrow key to move the snake to the left.
- Use the RIGHT arrow key to move the snake to the right.

The game starts with a single food item on the playing field. When the snake's head occupies the same grid space as the food, the snake consumes the food, triggering growth. Each food item typically increases the snake's length by one unit. After a food item is consumed, a new item appears somewhere else on the playing field.

The game ends when the snake collides with its own body or the walls of the playing field.

## 🏆 Scoring

Each food item consumed increases the player's score. The score is displayed at the top left corner of the game window.

## 💻 Running the Game

To start the game, navigate to the directory containing the game files in your terminal and run the following command:

`python main.py`

Enjoy the game!

## 📚 Documentation

For more information on the game mechanics and code structure, please refer to the comments in the Python files:

- `main.py`: This is the main entry point of the game. It creates an instance of the Game class and starts the game loop.
- `game.py`: This file contains the Game class which handles the game loop, events, and rendering the game on the screen.
- `entities.py`: This file contains the Snake, Food, Point, and Direction classes.

```
