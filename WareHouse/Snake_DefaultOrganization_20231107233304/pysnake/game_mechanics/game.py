"""
This file contains the Game class, which controls the game loop, user input, and game state.
"""
from __future__ import annotations

from dataclasses import dataclass

import pygame.display
import pygame.event
from pysnake.directions import Direction
from pysnake.event_handler import EventBus
from pysnake.event_handler import KeyPress
from pysnake.event_handler import Quit
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
        self.event_bus = EventBus([])
        self.running = True

    def event_handler(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.event_bus.write(Quit())
            elif event.type == pygame.KEYDOWN:
                self.event_bus.write(KeyPress(event.key))

    def run(self):
        while self.running:
            self.event_handler()
            try:
                for quit_event in self.event_bus.find_by(Quit):
                    print("Quitting snakepy!")
                    self.running = False
                    break
            except KeyError:
                self.running = True
            try:
                for keypress_event in self.event_bus.find_by(KeyPress):
                    if keypress_event.key in list(Direction):
                        self.session.snake.move(Direction(keypress_event.key))
            except KeyError:
                pass
            self.update_game_state()
            self.grid.draw(self.session.snake, self.session.food)
            pygame.time.delay(100)

    def update_game_state(self):
        self.running = self.session.snake.alive
        if self.session.snake.head.position == self.session.food.position:
            self.session.snake.grow = True
            self.session.food = Food.spawn()
            self.session.score.increase()
