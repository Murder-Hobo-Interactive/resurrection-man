from typing import Any
from abc import ABC, abstractmethod
from .types import Args, Kwargs


class Base(ABC):
    BASE_BLOCK = 16
    pass


class AbstractActor(Base):
    U = 0
    V = 0
    w = Base.BASE_BLOCK
    h = Base.BASE_BLOCK

    def __init__(
        self, controller: Any = None, view: Any = None, *args: Args, **kwargs: Kwargs
    ) -> None:
        self.controller = controller
        self.view = view
        self.x = 0
        self.y = 0

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def move_to(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @abstractmethod
    def update(self) -> None:
        pass

    def draw(self) -> None:
        self.view.blt(self.x, self.y, 0, self.U, self.V, self.w, self.h, 14)


class AbstractController(Base):
    def register(self, actor: AbstractActor) -> None:
        self.actor = actor

    @abstractmethod
    def update(self) -> None:
        pass
