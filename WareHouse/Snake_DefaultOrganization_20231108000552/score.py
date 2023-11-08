"""
This file contains the Score class which represents the score in the game.
"""
from __future__ import annotations

import pygame


class Score:
    def __init__(self):
        self.score = 0

    def increase_score(self):
        self.score += 1

    def draw(self, surface):
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(self.score), 1, (10, 10, 10))
        surface.blit(text, (10, 10))
