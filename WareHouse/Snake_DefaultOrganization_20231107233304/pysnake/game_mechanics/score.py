"""
This file contains the Score class, which controls the player's score.
"""
from __future__ import annotations


class Score:
    def __init__(self):
        self.score = 0

    def increase(self):
        self.score += 1

    def reset(self):
        self.score = 0
