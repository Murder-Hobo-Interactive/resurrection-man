import typing
from .abstracts import AbstractActor, AbstractController

class Enemy(AbstractActor):
    def __init__(self, controller:AbstractController, view: typing.Any):
        pass

    def update(self)->None:
        pass




if __name__ == "__main__":
    
    e = Enemy()