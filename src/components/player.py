from typing import Any
from .abstracts import AbstractActor, AbstractController
from .types import Args, Kwargs


class Player(AbstractActor):
    U = 16
    V = 64
    w = AbstractActor.BASE_BLOCK * 2
    h = AbstractActor.BASE_BLOCK * 2

    def __init__(
        self, controller: AbstractController, view: Any, *args: Args, **kwargs: Kwargs
    ) -> None:
        self.controller = controller
        self.controller.register(self)
        self.x = 10
        self.y = 10
        self.view = view

    def update(self) -> None:
        self.controller.update()

    def draw(self) -> None:
        self.view.blt(self.x, self.y, 0, self.U, self.V, self.w, self.h, 14)


if __name__ == "__main__":
    # this acts as a minimal test mostly to catch any type errors more easily
    from .keyboardcontroller import KeyboardController
    from .pyxelfactory import PyxelFactory

    v = PyxelFactory.create
    c = KeyboardController(v)
    e = Player(c, v)
