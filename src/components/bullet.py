from typing import Any
from .types import Args, Kwargs, Direction
from .abstracts import AbstractActor, AbstractController, Base
from .projectilecontroller import ProjectileController


class Bullet(AbstractActor):
    U = 0
    V = 16
    w = Base.BASE_BLOCK
    h = Base.BASE_BLOCK

    def update(self) -> None:
        self.controller.update()


class BulletFactory(Base):
    @classmethod
    def create(
        cls,
        x: int,
        y: int,
        dir: Direction,
        speed: int = 0,
        *args: Args,
        **kwargs: Kwargs
    ) -> None:
        # beware this might get a little funky if I'm passing the
        # same args to both the controller and the bullet itself
        # creating a footgun for myself later when those args shouldn't be the same
        pc = ProjectileController(dir=dir)
        cls.add_obj(Bullet(pc, x=x, y=y, speed=speed))
