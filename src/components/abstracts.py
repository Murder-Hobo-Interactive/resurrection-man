from abc import ABC, abstractmethod


class Base(ABC):
    # This is just here to be a base class
    pass

class AbstractActor(Base):
    @abstractmethod
    def __init__(self, controller)->None:  # type: ignore
        pass

    @abstractmethod
    def move(self, x: int, y: int)->None:
        pass
    
    @abstractmethod
    def move_to(self, x: int, y: int)->None:
        pass

    @abstractmethod
    def update(self)->None:
        pass

    @abstractmethod
    def draw(self)->None:
        pass

class AbstractController(Base):
    @abstractmethod
    def register(self, actor)->None: # type: ignore
        pass

    @abstractmethod
    def update(self)->None:
        pass