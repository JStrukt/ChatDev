"""
This file contains the Game class which handles the game logic.
"""
from __future__ import annotations


class Game:
    def __init__(self):
        self.board_size = 15
        self.board = [[None] * self.board_size for _ in range(self.board_size)]
        self.current_player = "black"

    def make_move(self, x, y):
        if self.board[x][y] is None:
            self.board[x][y] = self.current_player
            self.current_player = "white" if self.current_player == "black" else "black"

    def check_winner(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] is not None:
                    if (
                        self.check_horizontal(i, j)
                        or self.check_vertical(i, j)
                        or self.check_diagonal(i, j)
                    ):
                        return self.board[i][j]
        return None

    def check_horizontal(self, x, y):
        count = 0
        for i in range(y, min(y + 5, self.board_size)):
            if self.board[x][i] == self.board[x][y]:
                count += 1
            else:
                break
        return count == 5

    def check_vertical(self, x, y):
        count = 0
        for i in range(x, min(x + 5, self.board_size)):
            if self.board[i][y] == self.board[x][y]:
                count += 1
            else:
                break
        return count == 5

    def check_diagonal(self, x, y):
        count = 0
        for i in range(5):
            if x + i < self.board_size and y + i < self.board_size:
                if self.board[x + i][y + i] == self.board[x][y]:
                    count += 1
                else:
                    break
        if count == 5:
            return True
        count = 0
        for i in range(5):
            if x + i < self.board_size and y - i >= 0:
                if self.board[x + i][y - i] == self.board[x][y]:
                    count += 1
                else:
                    break
        return count == 5
