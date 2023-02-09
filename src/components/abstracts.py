from typing import Any, List
from abc import ABC, abstractmethod
from collections.abc import Callable
from .types import Args, Kwargs, EdgeBehavior
from .utils import clamp
from .pyxelfactory import PyxelFactory


class Base(ABC):
    # "global" variables will go here
    # GAME_OBJECTS not static but I want to handle the access separately
    GAME_OBJECTS: List[Any] = []
    BASE_BLOCK = 16
    GAME_WIDTH = 420
    GAME_HEIGHT = 260
    _pyxel = PyxelFactory.create()

    @staticmethod
    def add_obj(obj: Any) -> None:
        Base.GAME_OBJECTS.append(obj)

    @staticmethod
    def get_game_objects() -> List[Any]:
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
        edge_behavior: EdgeBehavior = EdgeBehavior.stop,
        *args: Args,
        **kwargs: Kwargs
    ) -> None:
        self.controller = controller
        self.x = x
        self.y = y
        self.speed = speed
        self.controller.register(self)
        # todo: maybe add different config for looping screen
        # or leaving screen
        self.edge_behavior: EdgeBehavior = edge_behavior

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y
        if self.edge_behavior == EdgeBehavior.stop:
            self.x = clamp(self.x, 0, Base.GAME_WIDTH - self.w)
            self.y = clamp(self.y, 0, Base.GAME_HEIGHT - self.h)

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
    def register(self, actor: AbstractActor, *args: Args, **kwargs: Kwargs) -> None:
        self.actor = actor

    @abstractmethod
    def update(self) -> None:
        ...


class AbstractFiniteStateMachine(Base):
    def __init__(self, wait: int, *args: Args, **kwargs: Kwargs) -> None:
        self.wait = wait  # todo: I think this needs a better name
        self.state = self.state_start
        self._actor: AbstractActor
        # todo: I feel like there is a good way to use
        # a decorator here to decorate the state methods
        # todo: probably need to add checks that actor is set
        # before executing the state methods

    @property
    def actor(self) -> AbstractActor:
        return self._actor

    @actor.setter
    def actor(self, actor: AbstractActor) -> None:
        self._actor = actor

    @abstractmethod
    def state_start(self) -> None:
        raise NotImplementedError

    def update(self) -> None:
        self.state()
