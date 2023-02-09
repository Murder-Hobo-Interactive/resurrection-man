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
    def create(cls, *args: Args, **kwargs: Kwargs) -> Any:
        """
        kwarg params:
            x: int
            y: int
            dir: Direction
            speed: int
        """
        # beware this might get a little funky if I'm passing the
        # same args to both the controller and the bullet itself
        # creating a footgun for myself later when those args shouldn't be the same
        pc = ProjectileController(*args, **kwargs)
        return Bullet(pc, *args, **kwargs)
