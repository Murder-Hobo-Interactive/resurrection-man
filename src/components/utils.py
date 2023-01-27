import sys
import os
from typing import Union, TypeVar

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
