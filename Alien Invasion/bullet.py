import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, aiSetting, screen, ship):
		# create bullet right above the ship
		super(Bullet, self).__init__()
		self.screen = screen

		self.rect = pygame.Rect(0, 0, aiSetting.bullet_width, aiSetting.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		self.y = float(self.rect.y)

		self.color = aiSetting.bullet_color
		self.speed = aiSetting.bullet_speed
	
	def update(self):
		self.y -= self.speed
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)