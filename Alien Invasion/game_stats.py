class GameStats():
	def __init__(self, aiSetting):
		self.aiSetting = aiSetting
		self.reset_stats()
		self.alive = True

	def reset_stats(self):
		self.lives = self.aiSetting.init_lives