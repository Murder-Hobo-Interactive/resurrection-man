from components import KeyboardController, Player, PyxelFactory
class App:
    def __init__(self)->None:
        self._pyxel = PyxelFactory.create()
        self._pyxel.init(128, 128)
        self.keyboardInput = KeyboardController(self._pyxel)
        self.player = Player(self.keyboardInput, self._pyxel)
        self._pyxel.run(self.update, self.draw)

    def update(self)->None:
        self.player.update()
        self.keyboardInput.update()

    def draw(self)->None:
        # self._pyxel.cls(0)
        self.player.draw()

App()