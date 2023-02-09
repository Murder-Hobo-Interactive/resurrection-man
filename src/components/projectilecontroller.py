from typing import Any
from .abstracts import AbstractController, AbstractActor
from .types import Args, Kwargs, Dir


class ProjectileController(AbstractController):
    def __init__(self, _pyxel: Any, direction: Dir, *args: Args, **kwargs: Kwargs):
        self._pyxel = _pyxel
        self.actor: AbstractActor

    def update(self) -> None:
        pass
