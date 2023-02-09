from typing import Any
from .abstracts import AbstractController, AbstractActor
from .types import Args, Kwargs, Direction
from .utils import direction_to_vector


class ProjectileController(AbstractController):
    def __init__(self, dir: Direction = Direction.up, *args: Args, **kwargs: Kwargs):
        self.actor: AbstractActor
        self.direction = dir

    def update(self) -> None:
        self.actor.move(*direction_to_vector(self.direction, self.actor.speed))
