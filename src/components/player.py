from typing import Any
from .abstracts import AbstractActor, AbstractController

class Player(AbstractActor):
    U = 0
    V = 0
    w = 16
    h = 16
    def __init__(self, controller:AbstractController, view: Any, *args: tuple[Any], **kwargs: dict[str,Any])->None:
        self.controller = controller
        self.controller.register(self)
        self.x = 10
        self.y = 10
        self.view = view

    def update(self)->None:
        self.controller.update()

    def draw(self)->None:
        self.view.blt(self.x, self.y, 0, self.U, self.V, self.w, self.h, 14)


if __name__ == "__main__":
    # this acts as a minimal test mostly to catch any type errors more easily
    from .keyboardcontroller import KeyboardController
    from .pyxelfactory import PyxelFactory
    v = PyxelFactory.create
    c = KeyboardController(v)
    e = Player(c, v)
