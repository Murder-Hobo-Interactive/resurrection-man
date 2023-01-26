import pyxel  # type: ignore
from components import keyboardcontroller, player
class App:
    def __init__(self)->None:
        pyxel.init(800, 600)
        pyxel.run(self.update, self.draw)
        keyboardInput = keyboardcontroller()
        self.player = player(keyboardInput)

    def update(self)->None:
        self.player.update()

    def draw(self)->None:
        pyxel.cls(0)
        self.player.draw()

App()