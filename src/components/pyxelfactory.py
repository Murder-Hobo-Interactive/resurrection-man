import pyxel # type: ignore

class PyxelFactory:
    @classmethod
    def create(cls):
        return pyxel
    
    # todo add config for fake pyxel