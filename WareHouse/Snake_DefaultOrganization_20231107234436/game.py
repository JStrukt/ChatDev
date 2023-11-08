"""
This file contains the Game class which handles the game loop, events, and rendering the game on the screen.
"""
from __future__ import annotations

import pygame
from entities import Food
from entities import Snake


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.screen = pygame.display.set_mode((800, 600))

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.turn_up()
                    elif event.key == pygame.K_DOWN:
                        self.snake.turn_down()
                    elif event.key == pygame.K_LEFT:
                        self.snake.turn_left()
                    elif event.key == pygame.K_RIGHT:
                        self.snake.turn_right()
            if not self.snake.update(self.food):  # End the game if collision occurs
                return
            self.score += 1
            self.food.randomize_position()
            self.draw()
            pygame.display.update()
            clock.tick(10)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))
