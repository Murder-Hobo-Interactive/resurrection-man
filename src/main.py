from components import KeyboardController, Player, PyxelProxy
class App:
    def __init__(self)->None:
        self._pyxel = PyxelProxy()
        self._pyxel.init(800, 600)
        self.keyboardInput = KeyboardController(self._pyxel)
        self.player = Player(self.keyboardInput)
        self._pyxel.run(self.update, self.draw)

    def update(self)->None:
        self.player.update()
        self.keyboardInput.update()

    def draw(self)->None:
        self._pyxel.cls(0)
        self.player.draw()

App()