from .abstracts import AbstractController

class AIController(AbstractController):
    def __init__(self, *args, **kwargs):
        pass

    def register(self, actor) -> None:
        return super().register(actor)

    def update(self) -> None:
        return super().update()


class AIControllerFactory:
    @classmethod
    def create(cls):
        return AIController()

if __name__ == "__main__":
    AI = AIController()
