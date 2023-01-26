import typing
from .abstracts import AbstractActor, AbstractController

class Enemy(AbstractActor):
    U = 16
    V = 0
    def __init__(self, controller:AbstractController, view: typing.Any, *args, **kwargs):
        self.controller = controller
        self.controller.register(self)
        self.x = 24
        self.y = 24
        self.view = view

    def update(self)->None:
        pass


if __name__ == "__main__":
    # this acts as a minimal test mostly to catch any type errors more easily
    from .keyboardcontroller import KeyboardController
    from .pyxelfactory import PyxelFactory
    v = PyxelFactory.create
    c = KeyboardController(v)
    e = Enemy(c, v)