"""
This is the Score class. It handles the scoring system of the game.
"""
from __future__ import annotations

import pygame


class Score:
    def __init__(self):
        self.score = 0
        self.color = (255, 255, 255)
        self.font = pygame.font.Font(None, 36)

    def increment(self):
        self.score += 1

    def draw(self, surface):
        score_text = self.font.render(f"Score: {self.score}", 1, self.color)
        surface.blit(score_text, (5, 10))
