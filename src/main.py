import pyxel
from components import KeyboardController, Player
class App:
    def __init__(self)->None:
        pyxel.init(800, 600)
        keyboardInput = KeyboardController()
        self.player = Player(keyboardInput)
        pyxel.run(self.update, self.draw)

    def update(self)->None:
        self.player.update()

    def draw(self)->None:
        pyxel.cls(0)
        self.player.draw()

App()