"""
This is the main entry point for the Snake game. It initializes Pygame and starts the game.
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
