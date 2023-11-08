from __future__ import annotations

from typing import Tuple

import pygame.draw
from pysnake.datastructures import Color

from .grid import GRID_RESOLUTION
from .grid import GRID_SIZE

HB_SIZE: int = 1
HB_PIXEL_SIZE: int = GRID_SIZE // GRID_RESOLUTION  # 10 for the default grid size of 500


class Hitbox:
    def __init__(
        self,
        left: int,
        top: int,
        color: Color,
        size: int = HB_SIZE,
        pixel_multiplier: int = HB_PIXEL_SIZE,
    ):
        self.left = left
        self.top = top
        self.color = color
        self.size = size
        self.pixel_multiplier = pixel_multiplier
        self.rectangle_pixel_size = self.size * self.pixel_multiplier

    @property
    def position(self) -> tuple[int, int]:
        return (self.left, self.top)

    @property
    def rectangle(self) -> pygame.Rect:
        return pygame.Rect(
            self.left,
            self.top,
            self.rectangle_pixel_size,
            self.rectangle_pixel_size,
        )

    def draw(self, surface):
        pygame.draw.rect(
            surface=surface,
            color=self.color.value,
            rect=self.rectangle,
        )
