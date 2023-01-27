from typing import Any
from .abstracts import AbstractController, AbstractActor
from .types import Args, Kwargs


class KeyboardController(AbstractController):
    def __init__(self, _pyxel: Any, *args: Args, **kwargs: Kwargs) -> None:
        self._pyxel = _pyxel
        self.actor: AbstractActor

    def update(self) -> None:
        if not self.actor:
            return

        sprint = 1.0
        if self._pyxel.btn(self._pyxel.KEY_SHIFT):
            sprint = 2.0

        SPEED = int(sprint * 1.0)
        if self._pyxel.btn(self._pyxel.KEY_W):
            self.actor.move(0, -1 * SPEED)
        if self._pyxel.btn(self._pyxel.KEY_A):
            self.actor.move(-1 * SPEED, 0)
        if self._pyxel.btn(self._pyxel.KEY_S):
            self.actor.move(0, SPEED)
        if self._pyxel.btn(self._pyxel.KEY_D):
            self.actor.move(SPEED, 0)
