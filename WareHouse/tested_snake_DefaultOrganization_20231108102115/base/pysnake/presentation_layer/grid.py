"""
This file contains the Grid class, which controls the drawing of the game grid, snake, and food.
"""
from __future__ import annotations

from typing import Optional

import pygame.display
import pygame.draw
from pygame.surface import Surface


GRID_RESOLUTION: int = 10
GRID_SIZE: int = 500


class Grid:
    def __init__(self, surface: Surface | None = None):
        self.surface: Surface = (
            surface
            if surface is not None
            else pygame.display.set_mode((GRID_SIZE, GRID_SIZE))
        )

    def __enter__(self) -> Grid:
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.current_body = []
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pygame.quit()

    def reset_surface(self):
        self.surface.fill((0, 0, 0))

    def draw(self, snake, food):
        self.reset_surface()
        snake.draw(self.surface)
        food.draw(self.surface)
        pygame.display.flip()
