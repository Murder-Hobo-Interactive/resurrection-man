from typing import Any
from .types import Args, Kwargs
from .abstracts import AbstractActor, AbstractController, Base
from .projectilecontroller import ProjectileController


class Bullet(AbstractActor):
    U = 0
    V = 16
    w = Base.BASE_BLOCK
    h = Base.BASE_BLOCK

    def __init__(
        self,
        controller: Any = None,  # figure out how to change this Any to AbstractController
        view: Any = None,
        *args: Args,
        **kwargs: Kwargs
    ) -> None:
        self.controller = controller
        self.view = view
        self.x = kwargs.get("x", 0)
        self.y = kwargs.get("y", 0)
        self.speed = 42

    def update(self) -> None:
        self.controller.update()


class BulletFactory:
    @classmethod
    def create(cls) -> Any:
        pc = ProjectileController()
        return Bullet(
            pc,
        )
