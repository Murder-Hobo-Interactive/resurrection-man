from typing import Any, List
from abc import ABC, abstractmethod
from .types import Args, Kwargs
from .utils import clamp
from .pyxelfactory import PyxelFactory


class Base(ABC):
    # "global" variables will go here
    # GAME_OBJECTS not static but I want to handle the access separately
    GAME_OBJECTS: List[Any] = []
    BASE_BLOCK = 16
    _pyxel = PyxelFactory.create()

    def add_obj(self, obj: Any) -> None:
        Base.GAME_OBJECTS.append(obj)

    def get_game_objects(self) -> List[Any]:
        return Base.GAME_OBJECTS


class AbstractActor(Base):
    # U, V default to 0 for the default sprite
    # this will make it easy to debug when something is visible when it shouldn't be
    U = 0
    V = 0
    w = Base.BASE_BLOCK
    h = Base.BASE_BLOCK

    def __init__(
        self,
        controller: Any = None,  # figure out how to change this Any to AbstractController
        x: int = 0,
        y: int = 0,
        speed: int = 0,
        *args: Args,
        **kwargs: Kwargs
    ) -> None:
        self.controller = controller
        self.x = x
        self.y = y
        self.speed = speed

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
        self._pyxel.blt(self.x, self.y, 0, self.U, self.V, self.w, self.h, 14)


class AbstractController(Base):
    def register(self, actor: AbstractActor) -> None:
        self.actor = actor

    @abstractmethod
    def update(self) -> None:
        ...
