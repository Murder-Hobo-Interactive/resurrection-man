import sys
import os
from typing import Union, TypeVar
from .abstracts import Base
from .types import Direction

N = TypeVar("N", int, float)  # N for number


def resource_path(relative_path: str) -> str:
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS  # type: ignore
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def clamp(num: N, min_value: N, max_value: N) -> N:
    return max(min(num, max_value), min_value)


# maybe implement a vector2 class instead of returning a tuple
def direction_to_vector(dir: Direction) -> tuple[int, int]:
    dir_to_vec_map = {
        Direction.up: (0, -1),
        Direction.down: (0, 1),
        Direction.left: (-1, 0),
        Direction.right: (1, 0),
    }
    try:
        return dir_to_vec_map[dir]
    except KeyError:
        raise ValueError(f"Invalid direction: {dir}")
