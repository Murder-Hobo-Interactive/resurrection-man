from .types import Args, Kwargs, Direction
from .abstracts import Base
from .player import Player
from .enemy import EnemyFactory
from .keyboardcontroller import KeyboardController


class Background(Base):
    def __init__(self, U: int, V: int, w: int, h: int) -> None:
        self.name = "background"


# as much as I want to make another
# abstract class, I don't think I need to
class Scene(Base):
    def __init__(self) -> None:
        name = "scene"
        camera = None
        background = None

    def add_game_object(self, game_object: Base) -> None:
        Base.add_game_object(game_object)

    def create_player(
        self, x: int = 0, y: int = 0, *args: Args, **kwargs: Kwargs
    ) -> None:
        keyboardInput = KeyboardController(self._pyxel, *args, **kwargs)
        # there might be a reason to consider keeping the player object at index 0 ?
        Base.add_game_object(Player(controller=keyboardInput, x=x, y=y))

    def create_enemy(
        self, x: int = 0, y: int = 0, *args: Args, **kwargs: Kwargs
    ) -> None:
        self.add_game_object(EnemyFactory.create(*args, **kwargs))

    def create_n_enemies(self, n):
        for _ in range(n):
            self.create_enemy()

    def update(self) -> None:
        for each in self.get_game_objects():
            each.update()

    def draw(self) -> None:
        for each in self.get_game_objects():
            each.draw()
