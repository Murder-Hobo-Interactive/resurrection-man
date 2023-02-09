from typing import Any
from .abstracts import AbstractController, AbstractActor
from .types import Args, Kwargs, Direction
from .bullet import Bullet, BulletFactory
from .projectilecontroller import ProjectileController


class KeyboardController(AbstractController):
    def __init__(self, _pyxel: Any, *args: Args, **kwargs: Kwargs) -> None:
        self._pyxel = _pyxel
        self.actor: AbstractActor

    def update(self) -> None:
        if not self.actor:
            return

        sprint = 1.0
        if self._pyxel.btn(self._pyxel.KEY_SHIFT):
            sprint = 2.0

        # === Check for actor movement keys
        SPEED = int(sprint * 1.0)
        key_to_actor_direction = {
            self._pyxel.KEY_W: (0, -1 * SPEED),
            self._pyxel.KEY_A: (-1 * SPEED, 0),
            self._pyxel.KEY_S: (0, SPEED),
            self._pyxel.KEY_D: (SPEED, 0),
        }
        for key, direction_tuple in key_to_actor_direction.items():
            if self._pyxel.btn(key):
                self.actor.move(*direction_tuple)

        # === Check for bullet firing keys
        # todo: bullet speed (and other attributes) will eventually end up somewhere else
        # might end up being an attribute of a currently armed weapon
        bullet_speed = 10
        key_to_bullet_direction = {
            self._pyxel.KEY_UP: Direction.up,
            self._pyxel.KEY_DOWN: Direction.down,
            self._pyxel.KEY_LEFT: Direction.left,
            self._pyxel.KEY_RIGHT: Direction.right,
        }
        for key, direction in key_to_bullet_direction.items():
            if self._pyxel.btn(key):
                BulletFactory.create(direction, speed=bullet_speed)
