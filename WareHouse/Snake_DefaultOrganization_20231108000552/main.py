"""
This is the main file for the Snake game. It initializes the game and starts the game loop.
"""
from __future__ import annotations

import pygame
from game import Game


def main():
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()


if __name__ == "__main__":
    main()
