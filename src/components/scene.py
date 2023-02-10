from pickle import dump as p_dump, load as p_load
from .types import Args, Kwargs, Direction
from .abstracts import Base
from .player import PlayerFactory
from .enemy import EnemyFactory
from .keyboardcontroller import KeyboardController


class Background(Base):
    def __init__(self, U: int, V: int, w: int, h: int) -> None:
        self.name = "background"

    def update(self):
        pass

    def draw(self):
        pass


# as much as I want to make another
# abstract class, I don't think I need to
class Scene(Base):
    def __init__(self, filename: str = "") -> None:
        name = "scene"
        camera = None
        background = None
        self.game_objects = []
        if filename:
            pass

        Base.SCENE = self

    def create_player(
        self, x: int = 0, y: int = 0, *args: Args, **kwargs: Kwargs
    ) -> None:
        self.append(PlayerFactory.create(x=x, y=y, *args, **kwargs))

    def create_enemy(
        self, x: int = 0, y: int = 0, *args: Args, **kwargs: Kwargs
    ) -> None:
        self.append(EnemyFactory.create(*args, **kwargs))

    def create_n_enemies(self, n):
        for _ in range(n):
            self.create_enemy()

    def update(self) -> None:
        for each in self.game_objects:
            each.update()

    def draw(self) -> None:
        for each in self.game_objects:
            each.draw()

    def append(self, game_object: Base) -> None:
        self.game_objects.append(game_object)


class SceneLoader(Base):
    @staticmethod
    def load(filename: str) -> Scene:
        scene = p_load(open(filename, "rb"))
        return scene
