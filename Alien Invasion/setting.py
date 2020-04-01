import pygame
class Setting():
	def __init__(self):
		# screen settings:
		self.screen_width = 900
		self.screen_height = 600
		self.background_color = (230, 230, 230)

		# ship settings
		self.ship_speed = 3.0

		#bullet settings:
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_speed = 1
		self.bullet_color = (60, 60, 60)

		# alien settings
		self.alien_speed = 0.5
		self.alien_drop_speed = 10
		self.alien_direction = 1 # left: -1, right: 1

		# key settings
		self.key_left = pygame.K_a
		self.key_right = pygame.K_d
		self.key_shot = pygame.K_j

		# stats
		self.init_lives = 3