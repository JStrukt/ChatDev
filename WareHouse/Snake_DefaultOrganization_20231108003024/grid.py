"""
This is the Grid class. It handles the drawing of the grid on the screen.
"""
from __future__ import annotations

import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
GRIDSIZE = 20


class Grid:
    def __init__(self):
        self.color = (75, 75, 75)

    def draw(self, surface):
        if surface:  # Check if the surface object is valid
            for y in range(0, SCREEN_HEIGHT, GRIDSIZE):
                for x in range(0, SCREEN_WIDTH, GRIDSIZE):
                    if (x + y) % 2 == 0:
                        r = pygame.Rect((x, y), (GRIDSIZE, GRIDSIZE))
                        if (
                            pygame.display.get_init()
                        ):  # Check if the display module is initialized
                            pygame.draw.rect(surface, self.color, r)
