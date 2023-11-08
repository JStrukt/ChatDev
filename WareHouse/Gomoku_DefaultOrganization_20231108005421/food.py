"""
This file contains the Food class, which handles the food's position and drawing.
"""
from __future__ import annotations

import random

import pygame


class Food:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self, snake_body):
        while True:
            x = random.randint(0, self.width // self.cell_size - 1) * self.cell_size
            y = random.randint(0, self.height // self.cell_size - 1) * self.cell_size
            self.position = (x, y)
            if self.position not in snake_body:
                break

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            pygame.Rect(
                self.position[0],
                self.position[1],
                self.cell_size,
                self.cell_size,
            ),
        )
