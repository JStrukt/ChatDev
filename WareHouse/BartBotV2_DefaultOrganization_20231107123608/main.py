"""
This is the main file for the Simpson Tamagotchi game. It creates a game instance and starts the game.
"""
from __future__ import annotations

from game import Game


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
