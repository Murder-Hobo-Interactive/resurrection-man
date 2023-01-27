from typing import Any
from .abstracts import AbstractActor, AbstractController, AbstractFiniteStateMachine
from .aicontroller import AIController
from .types import Args, Kwargs


class Enemy(AbstractActor):
    U = 16
    V = 0

    def __init__(
        self, controller: AbstractController, view: Any, *args: Args, **kwargs: Kwargs
    ):
        self.controller = controller
        self.controller.register(self)
        self.x = 24
        self.y = 24
        self.view = view

    def update(self) -> None:
        pass


class EnemyFSM(AbstractFiniteStateMachine):
    ...


class EnemyFactory:
    @classmethod
    def create(cls, _pyxel: Any, *args: Args, **kwargs: Kwargs) -> Enemy:
        aiInput = AIController(*args, **kwargs)
        # aiInput.register()
        return Enemy(aiInput, _pyxel, *args, **kwargs)


if __name__ == "__main__":
    # this acts as a minimal test mostly to catch any type errors more easily
    from .keyboardcontroller import KeyboardController
    from .pyxelfactory import PyxelFactory

    v = PyxelFactory.create
    c = KeyboardController(v)
    e = Enemy(c, v)
