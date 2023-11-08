from __future__ import annotations

from enum import Enum

import pygame


class Direction(int, Enum):
    UP = -1
    DOWN = 1
    LEFT = 2
    RIGHT = -2

    @staticmethod
    def from_pygame(pygame_repr: int) -> Direction:
        CONV_TABLE = {
            pygame.K_UP: Direction.UP,
            pygame.K_DOWN: Direction.DOWN,
            pygame.K_LEFT: Direction.LEFT,
            pygame.K_RIGHT: Direction.RIGHT,
        }
        return CONV_TABLE[pygame_repr]
