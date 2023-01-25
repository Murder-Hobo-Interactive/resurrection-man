from abc import ABC, abstractmethod
from .AbstractActor import AbstractActor

class AbstractController(ABC):
    @abstractmethod
    def register(self, actor: AbstractActor)->None:
        pass
