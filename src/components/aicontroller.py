from typing import Any
from .abstracts import AbstractController, AbstractActor
from .types import Args, Kwargs


class AIController(AbstractController):
    def __init__(self, *args: Args, **kwargs: Kwargs):
        pass

    def register(self, actor: AbstractActor) -> None:
        return super().register(actor)

    def update(self) -> None:
        return super().update()


class AIControllerFactory:
    @classmethod
    def create(cls) -> AIController:
        return AIController()


if __name__ == "__main__":
    AI = AIController()
