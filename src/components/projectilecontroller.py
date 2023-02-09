from typing import Any
from .abstracts import AbstractController, AbstractActor
from .types import Args, Kwargs, Directions


class ProjectileController(AbstractController):
	def __init__(self, _pyxel: Any, direction: Direction, *args: Args, **kwargs: Kwargs):
		self._pyxel = _pyxel
		self.actor: AbstractActor

	def update(self):
		


