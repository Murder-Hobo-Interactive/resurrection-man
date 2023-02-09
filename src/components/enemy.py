from typing import Any
from .abstracts import AbstractActor, AbstractController, AbstractFiniteStateMachine
from .aicontroller import AIController, MoveAndPauseFSM
from .types import Args, Kwargs


class BasicEnemyFSM(AbstractFiniteStateMachine):
    def state_start(self) -> None:
        return super().state_start()

    def update(self) -> None:
        return super().update()


class Enemy(AbstractActor):
    U = 16
    V = 32
    w = AbstractActor.BASE_BLOCK * 2
    h = AbstractActor.BASE_BLOCK * 2

    def __init__(
        self,
        controller: AbstractController,
        fsm: AbstractFiniteStateMachine,
        *args: Args,
        **kwargs: Kwargs
    ):
        self.controller = controller
        self.fsm = fsm
        self.fsm.actor = self
        self.controller.register(self, fsm=fsm)  # type: ignore
        self.x = 24
        self.y = 24

    def update(self) -> None:
        pass


class EnemyFactory:
    @classmethod
    def create(cls, _pyxel: Any, *args: Args, **kwargs: Kwargs) -> Enemy:
        aiInput = AIController(*args, **kwargs)
        move_fsm = MoveAndPauseFSM(60)
        return Enemy(aiInput, move_fsm)


if __name__ == "__main__":
    # this acts as a minimal test mostly to catch any type errors more easily
    from .keyboardcontroller import KeyboardController
    from .pyxelfactory import PyxelFactory

    v = PyxelFactory.create()
    c = KeyboardController(v)
    e = Enemy(c, v)

    ai_c = AIController()
    e = Enemy(ai_c, v)
