"""
This file contains the SimpsonPet class which handles the game logic.
"""
from __future__ import annotations


class SimpsonPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.boredom = 0

    def feed(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        self.boredom -= 10
        if self.boredom < 0:
            self.boredom = 0

    def time_passes(self):
        self.hunger += 1
        self.boredom += 1

    def is_alive(self):
        return self.hunger < 50 and self.boredom < 50
