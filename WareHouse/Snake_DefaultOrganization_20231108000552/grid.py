"""
This file contains the Grid class which represents the grid in the game.
"""
from __future__ import annotations

import pygame


class Grid:
    def draw(self, surface):
        for y in range(0, 30):
            for x in range(0, 40):
                if (x + y) % 2 == 0:
                    r = pygame.Rect((x * 20, y * 20), (20, 20))
                    pygame.draw.rect(surface, (93, 216, 228), r)
                else:
                    rr = pygame.Rect((x * 20, y * 20), (20, 20))
                    pygame.draw.rect(surface, (84, 194, 205), rr)
