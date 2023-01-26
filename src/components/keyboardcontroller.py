from .abstracts import AbstractController, AbstractActor

class KeyboardController(AbstractController):
    def __init__(self, _pyxel)->None:
        self._pyxel = _pyxel
        self.actor: AbstractActor

    def register(self, actor: AbstractActor)->None:
        self.actor = actor

    def update(self)->None:
        if not self.actor:
            return

        if self._pyxel.btn(self._pyxel.KEY_W): # type: ignore
            self.actor.move(0, -1)
        if self._pyxel.btn(self._pyxel.KEY_A): # type: ignore
            self.actor.move(-1, 0)
        if self._pyxel.btn(self._pyxel.KEY_S): # type: ignore
            self.actor.move(0, 1)
        if self._pyxel.btn(self._pyxel.KEY_D): # type: ignore
            self.actor.move(1, 0)
        
