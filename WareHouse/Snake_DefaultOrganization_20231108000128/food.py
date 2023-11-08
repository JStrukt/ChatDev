"""
This file contains the Food class that represents the food in the game.
"""
from __future__ import annotations

import random

import pygame


class Food:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.position = self.generate_position()

    def generate_position(self):
        x = random.randint(0, self.grid_width - 1)
        y = random.randint(0, self.grid_height - 1)
        return x, y

    def draw(self, screen, grid_size):
        x, y = self.position
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (x * grid_size, y * grid_size, grid_size, grid_size),
        )
