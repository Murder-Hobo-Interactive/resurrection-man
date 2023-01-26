from typing import Any
from components import (
    KeyboardController,
    Player,
    PyxelFactory,
    EnemyFactory,
    constants as c,
)
import os
import sys


class App:
    def __init__(self, *args: tuple[Any], **kwargs: dict[str, Any]) -> None:
        # inversion of control of pyxel so that later
        # it's easy to either fake it for testing
        # or run headless as a game server
        self._pyxel = PyxelFactory.create(*args, **kwargs)
        self._pyxel.init(420, 260)

        # make a player entity
        keyboardInput = KeyboardController(self._pyxel, *args, **kwargs)
        self.player = Player(keyboardInput, self._pyxel, *args, **kwargs)

        self.gameObjects = []
        self.gameObjects.append(
            EnemyFactory.create(self._pyxel, *args, **kwargs)
        )  # todo: put this in a populate method

        self._pyxel.load(resource_path("resources.pyxres"))

        # --------------------
        # leave this at the end of init (nothing under it will run)
        self._pyxel.run(self.update, self.draw)

    def update(self) -> None:
        self.player.update()
        for x in self.gameObjects:
            x.update()

    def draw(self) -> None:
        self._pyxel.cls(0)
        self.player.draw()
        for x in self.gameObjects:
            x.draw()

        c.pyxel.text(35, 66, "Resurrection Man", c.pyxel.frame_count % 16)


# todo: move this to a utils module
def resource_path(relative_path: str) -> str:
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS  # type: ignore
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


App()
