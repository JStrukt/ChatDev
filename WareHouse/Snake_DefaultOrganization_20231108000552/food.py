"""
This file contains the Food class which represents the food in the game.
"""
from __future__ import annotations

import random

import pygame


class Food:
    def __init__(self):
        self.position = [random.randint(0, 39), random.randint(0, 29)]

    def respawn(self):
        self.position = [random.randint(0, 39), random.randint(0, 29)]

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            (255, 0, 0),
            pygame.Rect(self.position[0] * 20, self.position[1] * 20, 20, 20),
        )
