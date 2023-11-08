"""
This file contains the Snake class which represents the snake in the game.
"""
from __future__ import annotations

import pygame


class Snake:
    def __init__(self):
        self.position = [[5, 10], [4, 10], [3, 10]]
        self.direction = [1, 0]

    def move(self):
        head = self.position[0][:]
        head[0] += self.direction[0]
        head[1] += self.direction[1]
        self.position.insert(0, head)
        self.position.pop()

    def grow(self):
        self.position.append(self.position[-1])

    def collides_with_self(self):
        return self.position[0] in self.position[1:]

    def collides_with(self, obj):
        return self.position[0] == obj.position

    def change_direction(self, direction):
        if [a + b for a, b in zip(self.direction, direction)] == [0, 0]:
            return
        self.direction = direction

    def draw(self, surface):
        for p in self.position:
            pygame.draw.rect(
                surface,
                (0, 255, 0),
                pygame.Rect(p[0] * 20, p[1] * 20, 20, 20),
            )
