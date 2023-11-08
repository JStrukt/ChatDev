from __future__ import annotations

from dataclasses import dataclass
from enum import auto
from enum import Enum
from typing import Tuple


class Color(tuple, Enum):
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)


@dataclass
class Move:
    current_position: tuple[int, int]
    step_vector: tuple[int, int]


class Direction(int, Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


@dataclass
class DirectionConfig:
    direction: Direction
    key: int
    opposite: Direction
