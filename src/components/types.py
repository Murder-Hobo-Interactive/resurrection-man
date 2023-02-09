from typing import Any
from enum import Enum

# type aliases
Args = tuple[Any]
Kwargs = dict[str, Any]


class Directions(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
