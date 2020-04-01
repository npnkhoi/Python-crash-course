import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def runGame():
	# init game and screen
	pygame.init()
	aiSetting = Setting()
	stats = GameStats(aiSetting)
	screen = pygame.display.set_mode(
		(aiSetting.screen_width, aiSetting.screen_height))
	pygame.display.set_caption("Alien Invasion")

	ship = Ship(screen, aiSetting)
	bullets = Group()
	aliens = Group()

	gf.create_fleet(aiSetting, screen, aliens, ship)

	# start the main loop for the game
	while True:
		gf.check_events(aiSetting, screen, ship, bullets)
		# if stats.alive:
		ship.update()
		gf.update_aliens(aiSetting, screen, stats, aliens, ship, bullets)
		gf.update_bullets(aiSetting, screen, aliens, bullets, ship)
		gf.update_screen(aiSetting, screen, ship, aliens, bullets)
runGame()