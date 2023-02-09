from typing import Any
from .abstracts import AbstractController, AbstractActor
from .types import Args, Kwargs, Direction
from .utils import get_direction_vector


class ProjectileController(AbstractController):
    def __init__(
        self,
        dir: Direction = Direction.up,
        speed: int = 0,
        *args: Args,
        **kwargs: Kwargs
    ):
        self.x = x
        self.y = y
        self.actor: AbstractActor
        self.direction = dir
        self.speed = speed

    def update(self) -> None:
        self.actor.move(*get_direction_vector(self.direction, self.speed))
