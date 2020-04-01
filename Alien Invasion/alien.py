import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self, screen, aiSetting):
		super(Alien, self).__init__()
		self.screen = screen
		self.aiSetting = aiSetting

		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def touch_edge(self):
		return (self.rect.left <= self.screen.get_rect().left) or (
			self.rect.right >= self.screen.get_rect().right)

	def update(self):
		self.x += self.aiSetting.alien_speed * self.aiSetting.alien_direction
		self.rect.x = self.x