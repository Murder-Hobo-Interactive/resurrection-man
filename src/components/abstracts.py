from typing import Any
from abc import ABC, abstractmethod
from collections.abc import Callable
from .types import Args, Kwargs
from .utils import clamp


class Base(ABC):
    # "global" variables will go here
    BASE_BLOCK = 16


class AbstractActor(Base):
    # U, V default to 0 for the default sprite
    # this will make it easy to debug when something is visible when it shouldn't be
    U = 0
    V = 0
    w = Base.BASE_BLOCK
    h = Base.BASE_BLOCK

    def __init__(
        self,
        controller: Any = None,  # todo: figure out how to change this Any to AbstractController
        view: Any = None,
        *args: Args,
        **kwargs: Kwargs
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

    def move_toward(self, x: int, y: int, speed: int) -> None:
        self.x += int(clamp(x - self.x, -1 * speed, speed))
        self.y += int(clamp(y - self.y, -1 * speed, speed))

    @abstractmethod
    def update(self) -> None:
        ...

    def draw(self) -> None:
        self.view.blt(self.x, self.y, 0, self.U, self.V, self.w, self.h, 14)


class AbstractController(Base):
    def register(self, actor: AbstractActor) -> None:
        self.actor = actor

    @abstractmethod
    def update(self) -> None:
        ...


class AbstractFiniteStateMachine(Base):
    def __init__(
        self, wait: int, actor: AbstractActor, *args: Args, **kwargs: Kwargs
    ) -> None:
        self.wait = wait  # todo: I think this needs a better name
        self.actor = actor
        self.state = self.state_start

    @abstractmethod
    def state_start(self) -> None:
        ...

    @abstractmethod
    def update(self) -> None:
        ...
