from __future__ import annotations

from enum import Enum


class Color(tuple, Enum):
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
