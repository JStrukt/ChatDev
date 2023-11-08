"""
This is the main file for the Snake game. It imports and uses the other classes (Game, Snake, Food, Grid, and Score) to run the game.
"""
from __future__ import annotations

from pysnake.event_handler import EventHandler
from pysnake.game_mechanics import Game
from pysnake.presentation_layer import Grid


def main():
    EventHandler()
    with Grid() as grid:
        Game(grid).run()


if __name__ == "__main__":
    main()
