from __future__ import annotations

from typing import List

from pysnake.datastructures import Color
from pysnake.directions import Direction
from pysnake.movement import resolve_new_head
from pysnake.presentation_layer import GRID_SIZE
from pysnake.presentation_layer import HB_SIZE
from pysnake.presentation_layer import Hitbox


class Snake:
    def __init__(self):
        self.color = Color.GREEN
        self.body: list[Hitbox] = [
            Hitbox(10 * HB_SIZE, 5 * HB_SIZE, self.color),
            Hitbox(9 * HB_SIZE, 5 * HB_SIZE, self.color),
            Hitbox(8 * HB_SIZE, 5 * HB_SIZE, self.color),
        ]
        self.direction: Direction = Direction.RIGHT
        self.grow: bool = False
        self.alive: bool = True

    @property
    def size(self) -> int:
        return len(self.body)

    @property
    def head(self) -> Hitbox:
        return self.body[0]

    def move(self, requested_direction):
        grow: bool = False
        self.body.insert(
            0,
            Hitbox(
                **resolve_new_head(
                    self,
                    GRID_SIZE,
                    HB_SIZE,
                    requested_direction,
                ),
            ),
        )
        if self.collides_with(self.session.food):
            grow = True
        if not grow:
            self.body.pop()

    def collides_with(self, obj):
        collides: bool = True
        for my_own_body_part in self.body:
            if my_own_body_part.position in [
                external_body_part.position for external_body_part in obj.body
            ]:
                break
        else:
            collides = False
        return collides

    def eat(self, food):
        return self.collides_with(food)

    def draw(self, surface):
        for pxl in self.body:
            pxl.draw(surface)
