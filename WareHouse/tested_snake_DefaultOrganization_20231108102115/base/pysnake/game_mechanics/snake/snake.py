from __future__ import annotations

from typing import List

from pysnake.presentation_layer import Color
from pysnake.presentation_layer import Direction
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

    @property
    def size(self) -> int:
        return len(self.body)

    @property
    def head(self) -> Hitbox:
        return self.body[0]

    @property
    def identify_next_head(self) -> Hitbox:
        if self.direction == Direction.UP:
            return Hitbox(self.head.left, self.head.top - HB_SIZE, self.color)
        elif self.direction == Direction.DOWN:
            return Hitbox(self.head.left, self.head.top + HB_SIZE, self.color)
        elif self.direction == Direction.LEFT:
            return Hitbox(self.head.left - HB_SIZE, self.head.top, self.color)
        elif self.direction == Direction.RIGHT:
            return Hitbox(self.head.left + HB_SIZE, self.head.top, self.color)

    def move(self):
        self.direction = self.identify_next_direction
        self.body.insert(0, self.identify_next_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def collides_with(self, obj):
        return self.head.position == obj.body[0].position

    def check_collision(self):
        if (
            self.identify_next_head.left > (GRID_SIZE - HB_SIZE)
            or self.identify_next_head.left < 0
        ):
            return True
        if (
            self.identify_next_head.top > (GRID_SIZE - HB_SIZE)
            or self.identify_next_head.top < 0
        ):
            return True
        for body_part in self.body[1:]:
            if self.identify_next_head == body_part:
                return True
        return False

    def eat(self, food):
        return self.collides_with(food)

    def draw(self, surface):
        for pxl in self.body:
            pxl.draw(surface)
