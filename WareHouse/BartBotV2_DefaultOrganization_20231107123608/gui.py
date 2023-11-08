"""
This file contains the GUI class which handles user interaction.
"""
from __future__ import annotations


class GUI:
    def draw_intro(self):
        print("Welcome to the Simpson Tamagotchi game!")

    def get_user_input(self, prompt):
        return input(prompt)

    def update_status(self, pet):
        print(
            f"{pet.name}'s current status - Hunger: {pet.hunger}, Boredom: {pet.boredom}",
        )

    def draw_outro(self):
        print("Game over! Your pet has died of hunger or boredom.")
