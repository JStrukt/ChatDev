"""
The main file for the Bart Simpson Tamagotchi game.
"""
from __future__ import annotations

import tkinter as tk

from bart import Bart


class TamagotchiGame:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.bart_image = tk.PhotoImage(file="bart.png")
        self.bart_sprite = self.canvas.create_image(200, 200, image=self.bart_image)
        self.canvas.bind("<Button-1>", self.feed_bart)
        self.bart = Bart()
        self.update()  # Call the update method to continuously update the game state
        self.root.mainloop()

    def feed_bart(self, event):
        self.bart.feed()

    def update(self):
        self.bart.update()
        self.root.after(1000, self.update)


if __name__ == "__main__":
    game = TamagotchiGame()
