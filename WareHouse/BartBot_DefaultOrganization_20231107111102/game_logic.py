"""
Module for the main game logic.
"""
from __future__ import annotations

from bart import Bart

bart = Bart()


def update_game_state():
    bart.update()


def main_loop():
    while True:
        update_game_state()
        # TODO: Implement other game logic
