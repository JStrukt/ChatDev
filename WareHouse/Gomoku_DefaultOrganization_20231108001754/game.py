"""
This file contains the classes for the Snake game: Game, Snake, Food, Point, and Direction.
Now it also includes a scoring system.
"""
from __future__ import annotations

import random
from enum import Enum

import pygame


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Food:
    def __init__(self, x, y):
        self.position = Point(x, y)

    def spawn(self, width, height):
        self.position = Point(
            random.randint(0, width - 1),
            random.randint(0, height - 1),
        )


class Snake:
    def __init__(self, x, y):
        self.body = [Point(x, y)]
        self.direction = Direction.RIGHT

    def move(self):
        head = self.body[0]
        if self.direction == Direction.UP:
            self.body.insert(0, Point(head.x, head.y - 1))
        elif self.direction == Direction.DOWN:
            self.body.insert(0, Point(head.x, head.y + 1))
        elif self.direction == Direction.LEFT:
            self.body.insert(0, Point(head.x - 1, head.y))
        elif self.direction == Direction.RIGHT:
            self.body.insert(0, Point(head.x + 1, head.y))
        self.body.pop()

    def grow(self):
        self.body.append(None)

    def collides_with_self(self):
        return self.body[0] in self.body[1:]

    def check_border_collision(self, width, height, mode):
        head = self.body[0]
        if head.x < 0 or head.y < 0 or head.x >= width or head.y >= height:
            if mode == "classic":
                return True
            elif mode == "borderless":
                if head.x < 0:
                    self.body[0].x = width - 1
                elif head.x >= width:
                    self.body[0].x = 0
                elif head.y < 0:
                    self.body[0].y = height - 1
                elif head.y >= height:
                    self.body[0].y = 0
        return False


class Game:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.snake = Snake(self.width // 2, self.height // 2)
        self.food = Food(0, 0)
        self.food.spawn(self.width, self.height)
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def run(self):
        screen = pygame.display.set_mode((self.width * 10, self.height * 10))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.direction = Direction.UP
                    elif event.key == pygame.K_DOWN:
                        self.snake.direction = Direction.DOWN
                    elif event.key == pygame.K_LEFT:
                        self.snake.direction = Direction.LEFT
                    elif event.key == pygame.K_RIGHT:
                        self.snake.direction = Direction.RIGHT
            self.snake.move()
            if self.snake.collides_with_self():
                return
            if self.snake.check_border_collision(self.width, self.height, "classic"):
                return
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.food.spawn(self.width, self.height)
                self.score += 1
            self.render(screen)

    def render(self, screen):
        screen.fill((0, 0, 0))
        for point in self.snake.body:
            rect = pygame.Rect(point.x * 10, point.y * 10, 10, 10)
            pygame.draw.rect(screen, (0, 255, 0), rect)
        rect = pygame.Rect(self.food.position.x * 10, self.food.position.y * 10, 10, 10)
        pygame.draw.rect(screen, (255, 0, 0), rect)
        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(text, (10, 10))
        pygame.display.flip()
