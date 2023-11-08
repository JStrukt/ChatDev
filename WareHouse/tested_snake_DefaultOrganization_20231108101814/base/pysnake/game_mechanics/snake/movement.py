from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from pysnake.directions import Direction
from pysnake.directions import DirectionConfig
from pysnake.directions import get_config
from pysnake.presentation_layer import HB_SIZE

from .snake import Snake


def resolve_direction(
    snake: Snake,
    user_request: Direction,
) -> Direction:
    current: DirectionConfig = get_config(direction=snake.direction)
    if user_request == current.opposite:
        return current.direction
    return user_request


@dataclass
class Move:
    current_position: tuple[int, int]
    step_vector: tuple[int, int]


def resolve_move(snake: Snake, direction: Direction):
    if direction == Direction.UP:
        return Move(snake.head.position, (0, -HB_SIZE))
    elif direction == Direction.DOWN:
        return Move(snake.head.position, (0, HB_SIZE))
    elif direction == Direction.LEFT:
        return Move(snake.head.position, (-HB_SIZE, 0))
    elif direction == Direction.RIGHT:
        return Move(snake.head.position, (HB_SIZE, 0))


# def resolve_movement(
#         snake: Snake, direction: Direction
# ):
#     if direction == Direction.UP:
#         return Hitbox(self.head.left, self.head.top - HB_SIZE, self.color)
#     elif direction == Direction.DOWN:
#         return Hitbox(self.head.left, self.head.top + HB_SIZE, self.color)
#     elif direction == Direction.LEFT:
#         return Hitbox(self.head.left - HB_SIZE, self.head.top, self.color)
#     elif direction == Direction.RIGHT:
#         return Hitbox(self.head.left + HB_SIZE, self.head.top, self.color)
