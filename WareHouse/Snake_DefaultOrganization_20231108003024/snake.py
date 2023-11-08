"""
This is the Snake class. It handles the snake's movement, growth, and drawing on the screen.
"""
from __future__ import annotations

import random

import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
GRIDSIZE = 20
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (0, 255, 0)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (
            ((cur[0] + (x * GRIDSIZE)) % SCREEN_WIDTH),
            (cur[1] + (y * GRIDSIZE)) % SCREEN_HEIGHT,
        )
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        elif (
            cur[0] >= SCREEN_WIDTH
            or cur[0] < 0
            or cur[1] >= SCREEN_HEIGHT
            or cur[1] < 0
        ):
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRIDSIZE, GRIDSIZE))
