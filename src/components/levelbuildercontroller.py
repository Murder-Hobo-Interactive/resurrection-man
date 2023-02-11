from typing import List, Any, Callable
from .types import Args, Kwargs, EdgeBehavior
from .abstracts import (
    Base,
    AbstractActor,
    AbstractController,
    AbstractFiniteStateMachine,
)


class Cursor(AbstractActor):
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
        self.U = 0
        self.V = 48

    def update(self):
        self.x = self._pyxel.mouse_x
        self.y = self._pyxel.mouse_y

    def draw(self):
        self._pyxel.blt(self.x - 8, self.y - 8, 0, self.U, self.V, self.w, self.h, 14)


class LevelBuilderController(AbstractController):
    def __init__(self, *args, **kwargs):
        self.actor: AbstractActor
        self.creators: List[Callable] = []
        self._current_creator: Callable

    def update(self):
        if not self.actor:
            return

    def draw(self):
        pass
