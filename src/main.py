from components import KeyboardController, AIController, Player, Enemy, PyxelFactory, constants as c
import os
import sys

class App:
    def __init__(self, *args, **kwargs)->None:
        # inversion of control of pyxel so that later
        # it's easy to either fake it for testing
        # or run headless as a game server
        self._pyxel = PyxelFactory.create(*args, **kwargs)
        self._pyxel.init(420, 260)

        # make a player entity
        keyboardInput = KeyboardController(self._pyxel, *args, **kwargs)
        self.player = Player(keyboardInput, self._pyxel, *args, **kwargs)

        # make an enemy entity
        aiInput = AIController(*args, **kwargs)
        self.enemy = Enemy(aiInput, self._pyxel, *args, **kwargs)
        self._pyxel.load(resource_path("resources.pyxres"))


        # --------------------
        # leave this at the end of init (nothing under it will run)
        self._pyxel.run(self.update, self.draw)
        

    def update(self)->None:
        self.player.update()

    def draw(self)->None:
        self._pyxel.cls(0)
        self.player.draw()
        c.pyxel.text(35, 66, "Resurrection Man", c.pyxel.frame_count % 16)


# todo: move this to a utils module
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

App()
