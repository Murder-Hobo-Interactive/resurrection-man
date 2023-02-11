from typing import Any
from components import (
    Base,
    constants as c,
    utils as u,
    SceneLoader,
    Args,
    Kwargs,
)
import typer

cli = typer.Typer()


class App(Base):
    def __init__(self, build=False, *args: Args, **kwargs: Kwargs) -> None:
        # inversion of control of pyxel so that later
        # it's easy to either fake it for testing
        # or run headless as a game server
        self._pyxel.init(self.GAME_WIDTH, self.GAME_HEIGHT)
        self._pyxel.load(u.resource_path("resources.pyxres"))
        if build:
            SceneLoader.load("scenes/create_scene.pickle")
        else:
            SceneLoader.load("scenes/default_scene.pickle")

        # --------------------
        # leave this at the end of init (nothing under it will run)
        self._pyxel.run(self.update, self.draw)

    def update(self) -> None:
        for x in self.get_game_objects():
            x.update()

    def draw(self) -> None:
        self._pyxel.cls(0)  # clear screen
        for x in self.get_game_objects():
            x.draw()

        c.pyxel.text(35, 66, "Resurrection Man", c.pyxel.frame_count % 16)


@cli.command()
def default(build: bool = False):
    App(build=build)


if __name__ == "__main__":
    cli()
