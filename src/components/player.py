from .abstractactor import AbstractActor
from .abstractcontroller import AbstractController

class Player(AbstractActor):
    U = 0
    V = 0

    def __init__(self, controller:AbstractController)->None:
        self.controller = controller
        self.controller.register(self)
        self.x = 0
        self.y = 0

    def move(self, x:int, y:int)->None:
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        pass
