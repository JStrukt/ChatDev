"""
This file contains the Snake class that represents the snake in the game.
"""
from __future__ import annotations

import pygame


class Snake:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.body = [(grid_width // 2, grid_height // 2)]
        self.direction = "right"

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "down":
            new_head = (head_x, head_y + 1)
        elif self.direction == "left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "right":
            new_head = (head_x + 1, head_y)
        self.body.insert(0, new_head)
        self.body.pop()

    def change_direction(self, direction):
        if (
            (direction == "up" and self.direction != "down")
            or (direction == "down" and self.direction != "up")
            or (direction == "left" and self.direction != "right")
            or (direction == "right" and self.direction != "left")
        ):
            self.direction = direction

    def grow(self):
        tail_x, tail_y = self.body[-1]
        if self.direction == "up":
            new_tail = (tail_x, tail_y + 1)
        elif self.direction == "down":
            new_tail = (tail_x, tail_y - 1)
        elif self.direction == "left":
            new_tail = (tail_x + 1, tail_y)
        elif self.direction == "right":
            new_tail = (tail_x - 1, tail_y)
        self.body.append(new_tail)

    def head_position(self):
        return self.body[0]

    def draw(self, screen, grid_size):
        for segment in self.body:
            x, y = segment
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                (x * grid_size, y * grid_size, grid_size, grid_size),
            )
