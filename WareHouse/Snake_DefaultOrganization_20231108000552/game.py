"""
This file contains the Game class which controls the game loop, handles events, and manages the game state.
"""
from __future__ import annotations

import sys

import pygame
from food import Food
from grid import Grid
from score import Score
from snake import Snake


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.grid = Grid()
        self.score = Score()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(15)
            if self.snake.collides_with_self():
                running = False
                print("Game Over! Your score is: ", self.score.score)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction((1, 0))

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.snake.move()
        if self.snake.collides_with(self.food):
            self.snake.grow()
            self.food.respawn()
            self.score.increase_score()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.grid.draw(self.screen)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.score.draw(self.screen)
