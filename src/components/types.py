from typing import Any
from enum import Enum

# type aliases
Args = tuple[Any]
Kwargs = dict[str, Any]


# https://mypy.readthedocs.io/en/stable/literal_types.html#enums
class Direction(Enum):
    up = "up"
    down = "down"
    left = "left"
    right = "right"


class EdgeBehavior(Enum):
    wrap = "wrap"
    bounce = "bounce"
    stop = "stop"
    destroy = "destroy"
    loop = "loop"
