import random
from typing import Any
from .abstracts import AbstractController, AbstractActor, AbstractFiniteStateMachine
from .types import Args, Kwargs, Direction
from .utils import direction_to_vector


class MoveAndPauseFSM(AbstractFiniteStateMachine):
    def __init__(self, wait: int, *args: Args, **kwargs: Kwargs) -> None:
        super().__init__(wait, *args, **kwargs)
        self.state_count = 0
        self.move_speed = 1
        self.dir = Direction.up

    def state_start(self) -> None:
        self.state = self.state_move

    def state_move(self) -> None:
        if self.state_count < self.wait:
            self.state_count += 1
            self.actor.move(*direction_to_vector(self.dir, self.move_speed))
        else:
            self.state_count = 0
            self.state = self.state_pause

    def state_pause(self) -> None:
        if self.state_count < self.wait:
            self.state_count += 1
            self.dir = random.choice([d for d in Direction])
        else:
            self.state_count = 0
            self.state = self.state_move


class AIController(AbstractController):
    def __init__(self, *args: Args, **kwargs: Kwargs):
        self.actor: AbstractActor
        self.fsm: AbstractFiniteStateMachine

    def register(self, actor: AbstractActor, *args: Args, **kwargs: Kwargs) -> None:
        self.actor = actor
        self.fsm = kwargs.get("fsm", MoveAndPauseFSM(60, self.actor))  # type: ignore

    def update(self) -> None:
        self.fsm.update()


class AIControllerFactory:
    @classmethod
    def create(cls) -> AIController:
        return AIController()


if __name__ == "__main__":
    AI = AIController()
