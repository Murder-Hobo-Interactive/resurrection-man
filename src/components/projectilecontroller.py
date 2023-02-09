from typing import Any
from .abstracts import AbstractController, AbstractActor
from .types import Args, Kwargs, Direction


class ProjectileController(AbstractController):
    def __init__(self, dir: Direction, *args: Args, **kwargs: Kwargs):
        self.actor: AbstractActor
        self.direction = dir

    def update(self) -> None:
        pass
