from typing import Any
from .abstracts import AbstractActor, Base
from .types import Args, Kwargs
from .keyboardcontroller import KeyboardController


class Player(AbstractActor):
    U = 16
    V = 64
    w = AbstractActor.BASE_BLOCK * 2
    h = AbstractActor.BASE_BLOCK * 2

    def update(self) -> None:
        self.controller.update()

    def draw(self) -> None:
        self._pyxel.blt(self.x, self.y, 0, self.U, self.V, self.w, self.h, 14)


class PlayerFactory(Base):
    @classmethod
    def create(
        cls,
        x: int = 0,
        y: int = 0,
        controller: Any = None,  # figure out how to change this Any to AbstractController
        *args: Args,
        **kwargs: Kwargs
    ) -> Player:
        keyboardInput = KeyboardController(*args, **kwargs)
        # there might be a reason to consider keeping the player object at index 0 in the game objects list?

        return Player(controller=keyboardInput, x=x, y=y)


if __name__ == "__main__":
    # this acts as a minimal test mostly to catch any type errors more easily

    c = KeyboardController()
    e = Player(controller=c)
