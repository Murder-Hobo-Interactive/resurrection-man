from typing import Any, List
from abc import ABC, abstractmethod
from collections.abc import Callable
from functools import wraps

from .types import Args, Kwargs, EdgeBehavior
from .utils import clamp
from .pyxelfactory import PyxelFactory


class Base(ABC):
    # "global" variables will go here
    # GAME_OBJECTS not const but I want to handle the access separately
    # the idea here is to make it look scary so I don't use it directly
    SCENE: Any
    SCENE_EXT = ".pickle"
    BASE_BLOCK = 16
    GAME_WIDTH = 420
    GAME_HEIGHT = 260

    _pyxel = PyxelFactory.create()

    @staticmethod
    def remove_first() -> None:
        Base.SCENE.pop(0)

    @staticmethod
    def set_scene(scene: Any) -> None:
        Base.SCENE = scene

    @staticmethod
    def add_game_object(obj: Any) -> None:
        Base.SCENE.append(obj)

    @staticmethod
    def get_game_objects() -> Any:
        return Base.SCENE.game_objects


class Decorators:
    @staticmethod
    def movement(func: Any) -> Any:  # I'll come back for this
        @wraps(func)
        def _wrapper(self, *args: Args, **kwargs: Kwargs) -> None:  # type: ignore
            # before movement
            func(self, *args, **kwargs)
            # after movement
            if self.edge_behavior == EdgeBehavior.stop:
                self.x = clamp(self.x, 0, Base.GAME_WIDTH - self.w)
                self.y = clamp(self.y, 0, Base.GAME_HEIGHT - self.h)
            if self.edge_behavior == EdgeBehavior.loop:
                self.x = self.x % Base.GAME_WIDTH
                self.y = self.y % Base.GAME_HEIGHT
            if self.edge_behavior == EdgeBehavior.bounce:
                if self.x < 0 or self.x > Base.GAME_WIDTH - self.w:
                    self.speed *= -1
                if self.y < 0 or self.y > Base.GAME_HEIGHT - self.h:
                    self.speed *= -1
            if self.edge_behavior == EdgeBehavior.destroy:
                if self.x < 0 or self.x > Base.GAME_WIDTH - self.w:
                    self.destroy()
                if self.y < 0 or self.y > Base.GAME_HEIGHT - self.h:
                    self.destroy()

        return _wrapper

class AbstractItem(Base):
    def __init__(self):
        pass
        
class AbstractActor(Base):
    """
    Abstract class for all actors in the game
    """

    # U, V default to 0 for the default sprite
    # this will make it easy to debug when something is visible when it shouldn't be
    U = 0
    V = 0
    w = Base.BASE_BLOCK
    h = Base.BASE_BLOCK

    def __init__(
        self,
        *args: Args,
        controller: Any = None,  # figure out how to change this Any to AbstractController
        x: int = 0,
        y: int = 0,
        speed: int = 0,
        edge_behavior: EdgeBehavior = EdgeBehavior.stop,
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

    @Decorators.movement
    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    @Decorators.movement
    def move_to(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @Decorators.movement
    def move_toward(self, x: int, y: int, speed: int) -> None:
        self.x += int(clamp(x - self.x, -1 * speed, speed))
        self.y += int(clamp(y - self.y, -1 * speed, speed))

    def destroy(self) -> None:
        Base.SCENE.game_objects.remove(self)

    @abstractmethod
    def update(self) -> None:
        ...

    def draw(self) -> None:
        self._pyxel.blt(self.x, self.y, 0, self.U, self.V, self.w, self.h, 14)

    @classmethod
    def preview(cls, x: int, y: int) -> None:
        # maybe make it flash when previewing or some visual indication that it isn't placed
        cls._pyxel.blt(x, y, 0, cls.U, cls.V, cls.w, cls.h, 14)


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
