from typing import Any
from .abstracts import AbstractController, AbstractActor, AbstractFiniteStateMachine
from .types import Args, Kwargs


class AIController(AbstractController):
    def __init__(self, *args: Args, **kwargs: Kwargs):
        self.actor: AbstractActor
        self.fsm: AbstractFiniteStateMachine | None

    def register(
        self, actor: AbstractActor, fsm: AbstractFiniteStateMachine | None = None
    ) -> None:
        self.actor = actor
        self.fsm = fsm

    def update(self) -> None:
        return super().update()


class AIControllerFactory:
    @classmethod
    def create(cls) -> AIController:
        return AIController()


if __name__ == "__main__":
    AI = AIController()
