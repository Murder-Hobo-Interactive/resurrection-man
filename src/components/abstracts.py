from abc import ABC, abstractmethod


class Base(ABC):
    BASE_BLOCK = 16
    pass

class AbstractActor(Base):
    U = 0
    V = 0
    w = Base.BASE_BLOCK
    h = Base.BASE_BLOCK
    def __init__(self, controller, view)->None:  # type: ignore
        self.controller = controller
        self.view = view
        self.x = 0
        self.y = 0


    @abstractmethod
    def move(self, x: int, y: int)->None:
        pass
    
    @abstractmethod
    def move_to(self, x: int, y: int)->None:
        pass

    @abstractmethod
    def update(self)->None:
        pass

    def draw(self)->None:
        self.view.blt(self.x, self.y, 0, self.U, self.V, self.w, self.h, 14)


class AbstractController(Base):
    @abstractmethod
    def register(self, actor)->None: # type: ignore
        pass

    @abstractmethod
    def update(self)->None:
        pass