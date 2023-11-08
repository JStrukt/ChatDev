"""
This is the Food class. It handles the food's spawning and drawing on the screen.
"""
from __future__ import annotations

import random

import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
GRIDSIZE = 20


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 0, 0)
        # Removed the argument from the randomize_position method

    def randomize_position(
        self,
        snake_positions,
    ):  # Added the snake_positions argument to the randomize_position method
        while True:
            self.position = (
                random.randint(0, SCREEN_WIDTH - GRIDSIZE),
                random.randint(0, SCREEN_HEIGHT - GRIDSIZE),
            )
            if self.position not in snake_positions:
                break

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            self.color,
            (self.position[0], self.position[1], GRIDSIZE, GRIDSIZE),
        )
