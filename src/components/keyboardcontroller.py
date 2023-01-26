from .abstracts import AbstractController, AbstractActor

class KeyboardController(AbstractController):
    def __init__(self, _pyxel, *args, **kwargs)->None:
        self._pyxel = _pyxel
        self.actor: AbstractActor

    def update(self)->None:
        if not self.actor:
            return
        
        sprint = 1.0
        if self._pyxel.btn(self._pyxel.KEY_SHIFT): # type: ignore
            sprint = 2.0
        
        SPEED = int(sprint * 1.0)
        if self._pyxel.btn(self._pyxel.KEY_W): # type: ignore
            self.actor.move(0, -1*SPEED)
        if self._pyxel.btn(self._pyxel.KEY_A): # type: ignore
            self.actor.move(-1*SPEED, 0)
        if self._pyxel.btn(self._pyxel.KEY_S): # type: ignore
            self.actor.move(0, SPEED)
        if self._pyxel.btn(self._pyxel.KEY_D): # type: ignore
            self.actor.move(SPEED, 0)
        
