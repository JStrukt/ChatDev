"""
This is the main file of the Gomoku game.
"""
from __future__ import annotations

import tkinter as tk

from game import Game


class GomokuApp:
    def __init__(self, master):
        self.master = master
        self.game = Game()
        self.board_size = 15
        self.cell_size = 30
        self.canvas_width = self.board_size * self.cell_size
        self.canvas_height = self.board_size * self.cell_size
        self.canvas = tk.Canvas(
            self.master,
            width=self.canvas_width,
            height=self.canvas_height,
        )
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()

    def draw_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")

    def on_click(self, event):
        x = event.x // self.cell_size
        y = event.y // self.cell_size
        self.game.make_move(x, y)
        self.draw_piece(x, y)
        winner = self.game.check_winner()
        if winner is not None:
            self.show_winner(winner)

    def draw_piece(self, x, y):
        x1 = x * self.cell_size
        y1 = y * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        self.canvas.create_oval(
            x1,
            y1,
            x2,
            y2,
            fill="black" if self.game.current_player == "black" else "white",
        )

    def show_winner(self, winner):
        self.canvas.unbind("<Button-1>")
        self.canvas.create_text(
            self.canvas_width // 2,
            self.canvas_height // 2,
            text=f"{winner.capitalize()} wins!",
            font=("Arial", 20),
            fill="red",
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = GomokuApp(root)
    root.mainloop()
