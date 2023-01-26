from typing import Any
import pyxel

class PyxelFactory:
    @classmethod
    def create(cls)->Any:
        return pyxel
    
    # todo add config for fake pyxel