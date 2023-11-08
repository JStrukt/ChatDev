# Snake Game

This is a simple yet engaging game developed using Python and Pygame. The game involves guiding a snake through a bounded plane, collecting food items, and avoiding collision with the snake's own body and walls.

## Main Features

- **Directional Control**: The snake is directed using keyboard arrows.
- **Continual Motion**: Once the game begins, the snake moves continuously and only changes direction upon player input.
- **Grid Movement**: The playing field is conceptualized as a grid, and the snake's movement is constrained to the grid lines.
- **Food Items**: Food items appear on the playing field at random locations. When the snake's head occupies the same grid space as the food, the snake consumes the food, triggering growth.
- **Scoring System**: Each food item increases the player's score.

## Quick Install

Before running the game, you need to install the required dependencies. You can do this by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

## How to Play

1. Run the `main.py` file to start the game. You can do this by navigating to the directory containing the file in your terminal and running the following command:

```bash
python main.py
```

2. Once the game starts, you can control the snake using the arrow keys on your keyboard. The snake cannot stop or reverse direction. It can only turn right or left.

3. The goal of the game is to eat as many food items as possible. Each food item the snake eats increases its length by one unit and the player's score by one point.

4. The game ends when the snake collides with its own body. The score at the end of the game is displayed in the terminal.

Enjoy the game and try to beat your high score!
