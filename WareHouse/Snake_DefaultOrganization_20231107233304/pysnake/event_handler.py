from __future__ import annotations

from dataclasses import dataclass

import pygame.event


@dataclass
class Event:
    pass


@dataclass
class Quit(Event):
    pass


@dataclass
class KeyPress(Event):
    key: int


class EventHandler:
    def __init__(self) -> None:
        self._quit: bool = False
        self._keypress: int | None = None

    @property
    def quit(self):
        ret_val = self._quit
        self._quit = False
        return ret_val

    @quit.setter
    def quit(self, value):
        self._quit = value

    @property
    def keypress(self):
        ret_val = self._keypress
        self._keypress = None
        return ret_val

    @keypress.setter
    def keypress(self, value):
        self._keypress = value

    def __call__(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                keypress: int = event.key
                self.keypress = keypress


@dataclass
class EventBus:
    events: list[Event]

    def find_by(self, event_type: type(Event)):
        for idx, event in enumerate(self.events):
            if isinstance(event, event_type):
                yield self.events.pop(idx)
        raise KeyError(
            f"No event of type {type(event_type)} was found on the EventBus."
        )

    # def read(self):
    #     for idx, _ in enumerate(self.events):
    #         yield self.events.pop(idx)

    def write(self, event: Event):
        self.events.append(event)
