from __future__ import annotations

from typing import Optional

import pygame.event


class EventHandler:
    def __init__(self):
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
