from .abstracts import AbstractController, AbstractActor

class KeyboardController(AbstractController):
    def __init__(self, _pyxel)->None:
        self._pyxel = _pyxel
        self.actor = None

    def register(self, actor: AbstractActor)->None:
        pass

    def update(self)->None:
        if not self.actor:
            return

        if self._pyxel.btn(self._pyxel.KEY_D): # type: ignore
            self.actor.move(1, 0)
