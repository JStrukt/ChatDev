"""
This is the main entry point of the game. It creates an instance of the Game class and starts the game loop.
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
