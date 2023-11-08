# Snake Game

This is a Python-based implementation of the classic Snake game. The game is built using the Pygame library and follows the SOLID principles of object-oriented design. The game features include continuous snake movement, food spawning and consumption, snake growth, and collision detection.

## Quick Install

To install the game and its dependencies, you need to have Python and pip installed on your system. If you don't have these, you can download Python [here](https://www.python.org/downloads/) and pip will be installed with it.

Once you have Python and pip, you can install Pygame, which is the only dependency for this game. To install Pygame, open your terminal or command prompt and type:

```bash
pip install pygame==2.0.1
```

## How to Play

To start the game, navigate to the directory containing the game files in your terminal or command prompt and type:

```bash
python main.py
```

This will start the game in a new window.

### Controls

The snake is controlled using the arrow keys:

- Up Arrow: Move Up
- Down Arrow: Move Down
- Left Arrow: Move Left
- Right Arrow: Move Right

The snake cannot reverse direction. For example, if it's moving right, it cannot immediately move left.

### Gameplay

The goal of the game is to eat as much food as possible. Each time the snake eats food (by moving its head to the same grid space as the food), it grows longer. The game ends when the snake collides with the game border or with its own body.

The food is represented by red squares that appear in random locations on the playing field. The snake is represented by a chain of green squares.

### Scoring

The score is determined by the amount of food the snake eats. Each food item increases the score by one. The current score is displayed in the terminal/command prompt.

## Enjoy the Game!

This implementation of Snake provides a simple and fun gaming experience. Enjoy playing, and try to beat your high score!
