import typing
from .abstracts import AbstractActor, AbstractController

class Enemy(AbstractActor):
    def __init__(self, controller:AbstractController, view: typing.Any, *args, **kwargs):
        pass

    def update(self)->None:
        pass


if __name__ == "__main__":
    # this acts as a minimal test mostly to catch any type errors more easily
    from .keyboardcontroller import KeyboardController
    from .pyxelfactory import PyxelFactory
    v = PyxelFactory.create
    c = KeyboardController(v)
    e = Enemy(c, v)