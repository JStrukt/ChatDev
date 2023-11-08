"""
This file contains the Snake, Food, Point, and Direction classes.
"""
from __future__ import annotations

import random

import pygame


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Direction:
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Snake:
    def __init__(self):
        self.body = [Point(10, 10)]
        self.direction = Direction.RIGHT

    def update(self, food):
        head = self.body[0]
        new_head = Point(head.x, head.y)
        if self.direction == Direction.UP:
            new_head.y -= 1
        elif self.direction == Direction.DOWN:
            new_head.y += 1
        elif self.direction == Direction.LEFT:
            new_head.x -= 1
        elif self.direction == Direction.RIGHT:
            new_head.x += 1
        # Check for collision with body
        for segment in self.body:
            if segment.x == new_head.x and segment.y == new_head.y:
                return False
        # Check for collision with boundaries
        if new_head.x < 0 or new_head.x > 79 or new_head.y < 0 or new_head.y > 59:
            return False
        if new_head.x == food.position.x and new_head.y == food.position.y:
            self.body.insert(0, new_head)
            return True
        self.body.pop()
        self.body.insert(0, new_head)
        return False

    def turn_up(self):
        if self.direction != Direction.DOWN:
            self.direction = Direction.UP

    def turn_down(self):
        if self.direction != Direction.UP:
            self.direction = Direction.DOWN

    def turn_left(self):
        if self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT

    def turn_right(self):
        if self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT

    def draw(self, surface):
        for point in self.body:
            pygame.draw.rect(
                surface,
                (0, 255, 0),
                pygame.Rect(point.x * 10, point.y * 10, 10, 10),
            )


class Food:
    def __init__(self):
        self.position = Point(0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = Point(random.randint(0, 79), random.randint(0, 59))

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            (255, 0, 0),
            pygame.Rect(self.position.x * 10, self.position.y * 10, 10, 10),
        )
