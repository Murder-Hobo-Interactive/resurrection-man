from typing_extensions import Protocol
from abc import ABC, abstractmethod
from components.abstractactor import AbstractActor

class AbstractController(ABC):
    @abstractmethod
    def register(self, actor: AbstractActor)->None:
        pass
