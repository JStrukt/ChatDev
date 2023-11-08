"""
This file contains the Game class that manages the game logic.
"""
from __future__ import annotations

import pygame
from food import Food
from snake import Snake


class Game:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.grid_size = 20
        self.grid_width = self.screen_width // self.grid_size
        self.grid_height = self.screen_height // self.grid_size
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.grid_width, self.grid_height)
        self.food = Food(self.grid_width, self.grid_height)
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update_game()
            self.update_screen()
            self.clock.tick(10)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction("up")
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction("down")
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction("left")
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction("right")

    def update_game(self):
        self.snake.move()
        self.check_collision()

    def check_collision(self):
        if self.snake.head_position() == self.food.position:
            self.snake.grow()
            self.food.generate_position()
        if self.snake.head_position() in self.snake.body[1:]:
            self.running = False

    def update_screen(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen, self.grid_size)
        self.food.draw(self.screen, self.grid_size)
        pygame.display.update()
