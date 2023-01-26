from typing_extensions import Protocol
from abc import ABC, abstractmethod
from components.abstractcontroller import AbstractController

class AbstractActor(ABC):
    @abstractmethod
    def __init__(self, controller: AbstractController)->None:
        pass

    @abstractmethod
    def move(self, x: int, y: int)->None:
        pass

    @abstractmethod
    def update(self)->None:
        pass

    @abstractmethod
    def draw(self)->None:
        pass
