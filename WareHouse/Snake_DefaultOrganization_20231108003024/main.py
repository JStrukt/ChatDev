"""
This is the main file for the Snake game. It initializes the game, handles user inputs, updates the game state, and renders the game on the screen.
"""
from __future__ import annotations

import pygame
from food import Food
from grid import Grid
from score import Score
from snake import Snake


class Game:
    def __init__(self):
        pygame.init()
        self.snake = Snake()
        self.food = Food()  # Removed the argument from the Food class
        self.grid = Grid()
        self.score = Score()
        self.surface = pygame.display.set_mode(
            (480, 480),
        )  # Added a surface for drawing
        self.run_game()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.snake.turn(event.key)
            self.snake.move()
            if self.snake.get_head_position() == self.food.position:
                self.food.randomize_position(
                    self.snake.positions,
                )  # Moved the snake's positions to the randomize_position method
                self.score.increment()
            self.grid.draw(
                self.surface,
            )  # Added the surface as an argument to the draw method
            self.snake.draw(
                self.surface,
            )  # Added the surface as an argument to the draw method
            self.food.draw(
                self.surface,
            )  # Added the surface as an argument to the draw method
            self.score.draw(
                self.surface,
            )  # Added the surface as an argument to the draw method
            pygame.display.update()


if __name__ == "__main__":
    Game()
