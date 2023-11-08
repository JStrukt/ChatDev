"""
This is the main file for the Snake game. It initializes the game, handles the game loop, and manages the game state.
"""
from __future__ import annotations

import food
import pygame
import snake

# Initialize Pygame
pygame.init()
# Set up some constants
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Create the snake and the food
snake = snake.Snake(WIDTH // 2, HEIGHT // 2, CELL_SIZE, WIDTH, HEIGHT)
food = food.Food(WIDTH, HEIGHT, CELL_SIZE)
food.randomize_position(
    snake.body,
)  # Fix: Call the randomize_position method after the Food object is created, passing the snake's body as an argument.
# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            snake.handle_keypress(event.key)
    # Game logic
    snake.move()
    if snake.game_over:
        running = False
    if snake.check_collision(food):
        snake.grow()
        food.randomize_position(snake.body)
    # Drawing
    screen.fill((0, 0, 0))
    snake.draw(screen)
    food.draw(screen)
    # Flip the display
    pygame.display.flip()
# Quit Pygame
pygame.quit()
