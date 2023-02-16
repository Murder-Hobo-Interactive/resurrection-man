from pickle import dump as p_dump, load as p_load
from typing import List, Any
from .types import Args, Kwargs, Direction
from .abstracts import Base
from .player import PlayerFactory
from .enemy import EnemyFactory
from .keyboardcontroller import KeyboardController
from .levelbuildercontroller import LevelBuilderController, Cursor


class Background(Base):
    def __init__(self, U: int, V: int, w: int, h: int) -> None:
        self.name = "background"

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pass


# as much as I want to make another
# abstract class, I don't think I need to
class Scene(Base):
    def __init__(self) -> None:
        name = "scene"
        camera = None
        background = None
        self.game_objects: List[Any] = []

    def create_player(
        self, x: int = 0, y: int = 0, *args: Args, **kwargs: Kwargs
    ) -> None:
        self.append(PlayerFactory.create(x=x, y=y))

    def create_enemy(
        self, x: int = 0, y: int = 0, *args: Args, **kwargs: Kwargs
    ) -> None:
        self.append(EnemyFactory.create(*args, **kwargs))  # type: ignore

    def create_n_enemies(self, n: int) -> None:
        for _ in range(n):
            self.create_enemy()

    def create_cursor(self, *args: Args, **kwargs: Kwargs) -> None:
        lbc = LevelBuilderController()
        self.append(Cursor(controller=lbc))

    def update(self) -> None:
        for each in self.game_objects:
            each.update()

    def draw(self) -> None:
        for each in self.game_objects:
            each.draw()

    def append(self, game_object: Base) -> None:
        self.game_objects.append(game_object)

    def pop(self, x: int) -> None:
        self.game_objects.pop(x)


class SceneLoader(Base):
    @staticmethod
    def load(filename: str) -> None:
        Base.SCENE = p_load(open(filename, "rb"))
