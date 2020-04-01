import sys, pygame
from bullet import Bullet
from alien import Alien
from game_stats import GameStats 
from time import sleep

def check_keydown(event, aiSetting, screen, ship, bullets):
	# print('Key down')
	if event.key == aiSetting.key_right:
		ship.moving_right = True
	elif event.key == aiSetting.key_left:
		ship.moving_left = True
	elif event.key == aiSetting.key_shot:
		new_bullet = Bullet(aiSetting, screen, ship)
		bullets.add(new_bullet)

def check_keyup(event, aiSetting, screen, ship, bullets):
	if event.key == aiSetting.key_right:
		ship.moving_right = False
	elif event.key == aiSetting.key_left:
		ship.moving_left = False

def check_events(aiSetting, screen, ship, bullets):
	# watch for keyboard and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown(event, aiSetting, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup(event, aiSetting, screen, ship, bullets)


def update_screen(aiSetting, screen, ship, aliens, bullets):
	# redraw the screen during each pass through the loop
	screen.fill(aiSetting.background_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)

	# make the most recently drawn screen visible
	pygame.display.flip()

def create_alien(aiSetting, screen, aliens, no_col, no_row):
	alien = Alien(screen, aiSetting)
	alien.x = alien.rect.width * (1 + 2 * no_col)
	alien.rect.x = alien.x
	alien.y = alien.rect.height * (1 + 2 * no_row)
	alien.rect.y = alien.y
	aliens.add(alien)


def create_fleet(aiSetting, screen, aliens, ship):
	alien = Alien(screen, aiSetting)
	no_cols = int((aiSetting.screen_width - alien.rect.width) 
		/ alien.rect.width / 2)
	no_rows = int((aiSetting.screen_height - alien.rect.height - ship.rect.height) 
		/ alien.rect.height / 2)

	for i in range(no_rows):
		for j in range(no_cols):
			create_alien(aiSetting, screen, aliens, j, i)

def check_edge(aiSetting, aliens):
	for alien in aliens.sprites():
		if alien.touch_edge():
			for alien in aliens.sprites():
				alien.y += aiSetting.alien_drop_speed
				alien.rect.y = alien.y
			aiSetting.alien_direction *= -1;
			break;

def check_alien_bottom(aiSetting, screen, stats, aliens, bullets, ship):
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen.get_rect().bottom:
			ship_hit(aiSetting, screen, stats, aliens, bullets, ship)

def ship_hit(aiSetting, screen, stats, aliens, bullets, ship):
	stats.lives -= 1
	sleep(0.5)

	if stats.lives > 0:
		aliens.empty()
		bullets.empty()
		create_fleet(aiSetting, screen, aliens, ship)
		ship.make_center()
		sleep(0.5)
	else:
		stats.alive = False

def update_aliens(aiSetting, screen, stats, aliens, ship, bullets):
	check_edge(aiSetting, aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship, aliens):
		# print("Ship hit!!!")
		ship_hit(aiSetting, screen, stats, aliens, bullets, ship)

	check_alien_bottom(aiSetting, screen, stats, aliens, bullets, ship)

def update_bullets(aiSetting, screen, aliens, bullets, ship):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
			# print(len(bullets))
	collison_check(aiSetting, screen, aliens, bullets, ship)

def collison_check(aiSetting, screen, aliens, bullets, ship):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if len(aliens) == 0:
		bullets.empty()
		create_fleet(aiSetting, screen, aliens, ship)