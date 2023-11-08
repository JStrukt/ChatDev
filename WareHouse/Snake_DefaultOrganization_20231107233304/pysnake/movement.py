from __future__ import annotations

from typing import List
from typing import Tuple

from pysnake.datastructures import Color
from pysnake.datastructures import Move
from pysnake.directions import Direction
from pysnake.directions import DirectionConfig
from pysnake.directions import get_config
from pysnake.exceptions import Collission
from pysnake.presentation_layer import GRID_SIZE
from pysnake.presentation_layer import HB_SIZE
from pysnake.presentation_layer import Hitbox


def resolve_direction(
    current_direction: Direction,
    user_request: Direction,
) -> Direction:
    current: DirectionConfig = get_config(direction=current_direction)
    if user_request == current.opposite:
        return current.direction
    return user_request


def resolve_move(
    head: tuple[int, int],
    hitbox_size: int,
    direction: Direction,
) -> Move:
    if direction == Direction.UP:
        return Move(head, (0, -1 * hitbox_size))
    elif direction == Direction.DOWN:
        return Move(head, (0, hitbox_size))
    elif direction == Direction.LEFT:
        return Move(head, (-1 * hitbox_size, 0))
    elif direction == Direction.RIGHT:
        return Move(head, (hitbox_size, 0))


def resolve_hitbox(color: Color, move: Move) -> Hitbox:
    ret_val = {
        "left": move.current_position[0] + move.step_vector[0],
        "top": move.current_position[1] + move.step_vector[1],
        "color": color,
    }
    return ret_val


def check_collision(
    head: tuple[int, int],
    body: list[tuple[int, int]],
    grid_size: int,
    hitbox_size: int,
    raise_exc: bool = True,
) -> bool:
    ret_val = False
    if head[0] > (grid_size - hitbox_size) or head[1] < 0:
        ret_val = True
    if head[0] > (grid_size - hitbox_size) or head[1] < 0:
        ret_val = True
    for body_part in body[1:]:
        if (head[0] == body_part[0]) and (head[0] == body_part[0]):
            ret_val = True
    if ret_val is True and raise_exc is True:
        raise Collission()


def resolve_new_head(
    user_request: Direction,
    current_direction: Direction,
    current_head: tuple[int, int],
    current_body: tuple[int, int],
    color: str,
    grid_size: int = GRID_SIZE,
    hitbox_size: int = HB_SIZE,
) -> dict:
    direction = resolve_direction(current_direction, user_request)
    move = resolve_move(current_head, hitbox_size, direction)
    if check_collision(current_head, current_body, grid_size, hitbox_size):
        raise Collission(user_request)
    return resolve_hitbox(color, move)
