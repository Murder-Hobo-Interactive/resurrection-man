import typing
from .abstracts import AbstractActor, AbstractController

class Player(AbstractActor):
    U = 0
    V = 0

    def __init__(self, controller:AbstractController, view: typing.Any)->None:
        self.controller = controller
        self.controller.register(self)
        self.x = 10
        self.y = 10
        self.view = view

    def move(self, x:int, y:int)->None:
        self.x += x
        self.y += y
    
    def move_to(self, x:int, y:int)->None:
        self.x = x
        self.y = y

    def update(self)->None:
        pass

