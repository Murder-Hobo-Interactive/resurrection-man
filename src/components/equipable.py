from .abstracts import AbstractItem

class Equipable(AbstractItem):
	def __init__(self):
		pass

class Gun(Equipable):
	
	def __init__(self):
		self.debounce = 0 #Debounce refers to the Time Between Bullets 
		self.fire_rate = 7 #This variable describes how fast the gun fires. Lower Number = More Automatic. Number of Frames between shots
	def fire(self):
		if (self.debounce == 0):
			self.debounce = self.fire_rate
			return True
		else:
			return False
	def update(self):
		if (self.debounce != 0):
			self.debounce -= 1

