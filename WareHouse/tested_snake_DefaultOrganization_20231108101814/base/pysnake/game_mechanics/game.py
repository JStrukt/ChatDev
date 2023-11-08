"""
This file contains the Game class, which controls the game loop, user input, and game state.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import pygame.display
import pygame.event
from pysnake.directions import DirectionConfig
from pysnake.event_handler import EventHandler
from pysnake.presentation_layer import Direction
from pysnake.presentation_layer import Grid

from .food import Food
from .score import Score
from .snake import Snake


@dataclass
class GameSession:
    snake: Snake
    food: Food
    score: Score

    @classmethod
    def from_defaults(cls) -> GameSession:
        return GameSession(Snake(), Food.spawn(), Score())


class Game:
    def __init__(
        self,
        grid: Grid,
        session: GameSession | None = None,
    ):
        self.session = session if session is not None else GameSession.from_defaults()
        self.grid = grid
        self.event_handler = EventHandler()
        self.running = True

    def run(self):
        while self.running:
            self.event_handler()
            if self.event_handler.quit:
                self.running = False
            if (keypress := self.event_handler.keypress) in list(Direction):
                self.session.snake.requested_direction = Direction(keypress)
            self.update_game_state()
            self.grid.draw(self.session.snake, self.session.food)
            pygame.time.delay(100)

    def update_game_state(self):
        self.session.snake.move()
        if self.session.snake.check_collision():
            self.running = False
        elif self.session.snake.head.position == self.session.food.position:
            self.session.snake.grow = True
            self.session.food = Food.spawn()
            self.session.score.increase()
