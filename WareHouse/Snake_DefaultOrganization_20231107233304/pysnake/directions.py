from __future__ import annotations

import pygame

from .datastructures import Direction
from .datastructures import DirectionConfig


ALL_DIRECTIONS = [
    DirectionConfig(Direction.UP, pygame.K_UP, Direction.DOWN),
    DirectionConfig(Direction.DOWN, pygame.K_DOWN, Direction.UP),
    DirectionConfig(Direction.LEFT, pygame.K_LEFT, Direction.RIGHT),
    DirectionConfig(Direction.RIGHT, pygame.K_RIGHT, Direction.LEFT),
]


def get_config(**kwargs) -> DirectionConfig:
    if (direction := kwargs.get("direction")) is not None:
        for _dir in ALL_DIRECTIONS:
            if _dir.direction == direction:
                return DirectionConfig
        raise ValueError
    elif (key := kwargs.get("key")) is not None:
        for _dir in ALL_DIRECTIONS:
            if _dir.key == key:
                return DirectionConfig
        raise ValueError
    elif (opposite := kwargs.get("opposite")) is not None:
        for _dir in ALL_DIRECTIONS:
            if _dir.opposite == opposite:
                return DirectionConfig
        raise ValueError
    raise ValueError
