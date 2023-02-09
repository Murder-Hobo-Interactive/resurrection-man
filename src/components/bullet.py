from .abstracts import AbstractActor, AbstractController
from .projectilecontroller import ProjectileController

class Bullet(AbstractActor):
	def __init__(
		self,
		controller: Any = None,  # figure out how to change this Any to AbstractController
		view: Any = None,
		*args: Args,
		**kwargs: Kwargs
		) -> None:
		self.controller = controller
		self.view = view
		self.x = 0
		self.y = 0
		self.speed = 42