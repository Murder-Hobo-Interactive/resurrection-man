import pyxel

class App:
    def __init__(self)->None:
        pyxel.init(160, 120)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self)->None:
        self.x = (self.x + 1) % pyxel.width

    def draw(self)->None:
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

App()