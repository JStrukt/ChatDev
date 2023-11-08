"""
This file contains the Game class which controls the game flow.
"""
from __future__ import annotations

from gui import GUI
from simpson_pet import SimpsonPet


class Game:
    def __init__(self):
        self.gui = GUI()
        self.pet = None

    def start(self):
        self.gui.draw_intro()
        pet_name = self.gui.get_user_input(
            "Choose your pet: Bart, Lisa, Maggie, Homer or Marge",
        )
        self.pet = SimpsonPet(pet_name)
        self.main_loop()

    def main_loop(self):
        while self.pet.is_alive():
            self.gui.update_status(self.pet)
            action = self.gui.get_user_input(
                "What do you want to do? (Feed / Play / Exit)",
            )
            while action.lower() not in ["feed", "play", "exit"]:
                print("Invalid action. Please try again.")
                action = self.gui.get_user_input(
                    "What do you want to do? (Feed / Play / Exit)",
                )
            if action.lower() == "feed":
                self.pet.feed()
            elif action.lower() == "play":
                self.pet.play()
            elif action.lower() == "exit":
                break
            self.pet.time_passes()
        self.gui.draw_outro()
