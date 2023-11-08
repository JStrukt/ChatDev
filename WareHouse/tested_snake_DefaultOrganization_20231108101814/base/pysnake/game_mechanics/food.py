"""
This file contains the Food class, which controls the food's location and respawn behavior.
"""
from __future__ import annotations

import random
from typing import Tuple

from pysnake.presentation_layer import Color
from pysnake.presentation_layer import GRID_RESOLUTION
from pysnake.presentation_layer import Hitbox


class Food:
    def __init__(self, left, top):
        self.color = Color.RED
        self.body = [
            Hitbox(
                left,
                top,
                self.color,
            ),
        ]

    @property
    def head(self) -> Hitbox:
        return self.body[0]

    @property
    def position(self) -> tuple[int, int]:
        return self.body[0].position

    @property
    def size(self) -> int:
        return len(self.body)

    @staticmethod
    def spawn() -> Food:
        random_left: int = random.randrange(1, GRID_RESOLUTION)
        random_top: int = random.randrange(1, GRID_RESOLUTION)
        return Food(random_left, random_top)

    def draw(self, surface):
        for pxl in self.body:
            pxl.draw(surface)
