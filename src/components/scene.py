from .types import Args, Kwargs, Direction
from .abstracts import Base

# as much as I want to make another
# abstract class, I don't think I need to
class Scene(Base):
    def __init__(self) -> None:
        name = "scene"

    def add_game_object(self, game_object: Base) -> None:
        Base.add_game_object(game_object)

    def update(self) -> None:
        for each in self.get_game_objects():
            each.update()

    def draw(self) -> None:
        for each in self.get_game_objects():
            each.draw()
