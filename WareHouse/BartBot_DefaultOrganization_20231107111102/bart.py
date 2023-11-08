"""
Module for Bart Simpson's attributes and behaviors.
"""
from __future__ import annotations


class Bart:
    def __init__(self):
        self.hunger = 0
        self.happiness = 100

    def feed(self):
        self.hunger -= 10
        self.happiness += 5

    def play(self):
        self.happiness += 10

    def update(self):
        self.hunger += 5
        self.happiness -= 5
        self.check_status()

    def check_status(self):
        if self.hunger >= 100:
            print("Bart is starving!")
        elif self.happiness <= 0:
            print("Bart is unhappy!")
