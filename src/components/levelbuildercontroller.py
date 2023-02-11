import pickle
from typing import List, Any, Callable
from .types import Args, Kwargs, EdgeBehavior
from .abstracts import (
    AbstractActor,
    AbstractController,
    Base,
)
from .utils import clamp
from .enemy import EnemyFactory
from .player import PlayerFactory


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
        self.controller.update()

    def draw(self):
        self._pyxel.blt(self.x - 8, self.y - 8, 0, self.U, self.V, self.w, self.h, 14)
        self.controller.draw()


class LevelBuilderController(AbstractController):
    def __init__(self, *args, **kwargs):
        self.actor: AbstractActor
        self.buildable: List[Callable] = [EnemyFactory.create, PlayerFactory.create]
        self.current_obj: AbstractActor = self.buildable[0]()
        self.i = 0
        self.outfilename = "new_level" + self.SCENE_EXT

    def update(self):
        if not self.actor:
            return
        i_change = clamp(self._pyxel.mouse_wheel, -1, 1)
        if i_change:
            self.i = (self.i + i_change) % len(self.buildable)
            self.current_obj = self.buildable[self.i]()

        if self._pyxel.btnp(self._pyxel.MOUSE_BUTTON_LEFT):
            Base.add_game_object(self.buildable[self.i](x=self.actor.x, y=self.actor.y))

        if self._pyxel.btnp(self._pyxel.KEY_Q):
            Base.remove_first()
            pickle.dump(Base.SCENE, open(self.outfilename, "wb"))

    def draw(self):
        self.current_obj.preview(self.actor.x, self.actor.y)
