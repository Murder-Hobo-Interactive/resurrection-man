from typing import Any
from .abstracts import (
    Base,
    AbstractActor,
    AbstractController,
    AbstractFiniteStateMachine,
)
from .aicontroller import AIController, MoveAndPauseFSM
from .types import Args, Kwargs, EdgeBehavior


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
        controller: AbstractController = AIController(),
        x: int = 0,
        y: int = 0,
        speed: int = 0,
        edge_behavior: EdgeBehavior = EdgeBehavior.stop,
        fsm: AbstractFiniteStateMachine = MoveAndPauseFSM(60),
        *args: Args,
        **kwargs: Kwargs
    ):
        super(Enemy, self).__init__(
            controller=controller,
            x=x,
            y=y,
            speed=speed,
            edge_behavior=edge_behavior,
        )
        self.fsm = fsm
        self.fsm.actor = self
        self.controller.register(self, fsm=fsm)

    def update(self) -> None:
        self.controller.update()


class EnemyFactory(Base):  # todo: probably implement a base factory class
    @classmethod
    def create(cls, *args: Args, **kwargs: Kwargs) -> Enemy:
        aiInput = AIController(*args, **kwargs)
        move_fsm = MoveAndPauseFSM(60)
        return Enemy(
            controller=aiInput,
            x=cls.GAME_WIDTH // 2,
            y=cls.GAME_HEIGHT // 2,
            fsm=move_fsm,
        )


if __name__ == "__main__":
    # this acts as a minimal test mostly to catch any type errors more easily
    from .keyboardcontroller import KeyboardController
    from .pyxelfactory import PyxelFactory

    v = PyxelFactory.create()
    c = KeyboardController(v)
    e = Enemy(c, v)

    ai_c = AIController()
    e = Enemy(ai_c, v)
