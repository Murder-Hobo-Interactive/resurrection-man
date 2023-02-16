from pickle import dump as p_dump, load as p_load
from typing import List, Any, List, Tuple, Union
from .types import Args, Kwargs, Direction
from .abstracts import Base, AbstractActor
from .player import PlayerFactory
from .enemy import EnemyFactory
from .keyboardcontroller import KeyboardController
from .levelbuildercontroller import LevelBuilderController, Cursor

QuadChild = Union["QuadTree", AbstractActor] | None


class QuadTree(Base):
    def __init__(
        self,
        actor_list: List[AbstractActor],
        parent: "QuadTree" | None = None,
        coords: Tuple[int, int, int, int] = (0, 0, 0, 0),  # x1, y1, x2, y2
    ) -> None:
        # if self.parent is None then we're at the root
        self.parent = parent
        # todo: initialize the children with the actor_list
        # 0: top left
        # 1: top right
        # 2: bottom left
        # 3: bottom right
        self.children: Tuple[QuadChild, QuadChild, QuadChild, QuadChild]
        self.coords = coords
        self.center = (self.coords[0] + self.coords[2]) // 2, (
            self.coords[1] + self.coords[3]
        ) // 2

    def which_coord(self, actor: AbstractActor) -> int:
        if actor.x < self.center[0]:
            return 0 if actor.y < self.center[1] else 2
        else:
            return 1 if actor.y < self.center[1] else 3

    def add(self, actor: AbstractActor) -> None:
        i = self.which_coord(actor)
        if self.children[i] and isinstance(self.children[i], QuadTree):
            self.children[i].add(actor)
        elif self.children[i] and isinstance(self.children[i], AbstractActor):
            tmp = self.children[i]
            self.children[i] = QuadTree(
                [tmp, actor],
                parent=self,
                coords=self.coords,  # todo: gotta split them coords
            )
        else:
            self.children[i] = actor


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
        self.quadtree = QuadTree(self.game_objects)

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
        self.check_for_collisions()
        for each in self.game_objects:
            each.update()

    def draw(self) -> None:
        # todo: handle things like background that need to be drawn first
        for each in self.game_objects:
            each.draw()

    def append(self, game_object: Base) -> None:
        self.game_objects.append(game_object)

    def pop(self, x: int) -> None:
        self.game_objects.pop(x)

    def check_for_collisions(self) -> None:
        pass


class SceneLoader(Base):
    @staticmethod
    def load(filename: str) -> None:
        Base.SCENE = p_load(open(filename, "rb"))
