from abc import ABC, abstractmethod
from .AbstractController import AbstractController

class AbstractActor(ABC):
    @abstractmethod
    def __init__(self, controller: AbstractController)->None:
        pass

    @abstractmethod
    def move(self, x: int, y: int)->None:
        pass
