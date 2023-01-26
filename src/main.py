from components import KeyboardController, Player, PyxelFactory, constants as c
import os
import sys

class App:
    def __init__(self)->None:
        self._pyxel = PyxelFactory.create()
        self._pyxel.init(128, 128)
        self.keyboardInput = KeyboardController(self._pyxel)
        self.player = Player(self.keyboardInput, self._pyxel)
        self._pyxel.run(self.update, self.draw)
        self._pyxel.load(resource_path("assets.pyxres"))

    def update(self)->None:
        self.player.update()
        self.keyboardInput.update()

    def draw(self)->None:
        self._pyxel.cls(0)
        self.player.draw()
        c.pyxel.text(35, 66, "Resurrection Man", c.pyxel.frame_count % 16)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

App()
