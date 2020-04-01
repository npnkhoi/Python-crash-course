import random
class Dice():
	def __init__(self, num_faces = 6):
		self.num_faces = num_faces

	def roll(self):
		return random.randint(1, self.num_faces)