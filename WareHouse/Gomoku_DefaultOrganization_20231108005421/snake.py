"""
This file contains the Snake class, which handles the snake's movement, growth, and collision detection.
"""
from __future__ import annotations

import pygame


class Snake:
    def __init__(self, x, y, cell_size, width, height):
        self.body = [(x, y)]
        self.direction = "UP"
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.game_over = False

    def handle_keypress(self, key):
        if key == pygame.K_UP and self.direction != "DOWN":
            self.direction = "UP"
        elif key == pygame.K_DOWN and self.direction != "UP":
            self.direction = "DOWN"
        elif key == pygame.K_LEFT and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif key == pygame.K_RIGHT and self.direction != "LEFT":
            self.direction = "RIGHT"

    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= self.cell_size
        elif self.direction == "DOWN":
            y += self.cell_size
        elif self.direction == "LEFT":
            x -= self.cell_size
        elif self.direction == "RIGHT":
            x += self.cell_size
        self.body.insert(0, (x, y))
        if (
            x < 0
            or y < 0
            or x >= self.width
            or y >= self.height
            or (x, y) in self.body[1:]
        ):
            self.game_over = True
        else:
            self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self, food):
        return self.body[0] == food.position

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                pygame.Rect(segment[0], segment[1], self.cell_size, self.cell_size),
            )
