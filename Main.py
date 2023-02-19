# Importing pygame module
import pygame
from pygame.locals import *

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
#window = pygame.display.set_mode()
window = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Player Movement')

# Initializing the clock
# Clocks are used to track and
# control the frame-rate of a game
clock = pygame.time.Clock()

# creating a variable to check the direction
# of movement
# We will change its value whenever
# the player changes its direction
direction = True


image = pygame.image.load('images/player.png')


x = 100
y = 100


velocity = 12

# 
run = True
while run:

	# FPS = 60
	clock.tick(60)

	# Hintergrund weiß gemacht
	window.fill((255, 255, 255))

	#spieler wird auf den passenden Kordinaten displayed
	if direction == True:
		window.blit(image, (x, y))
        #sprite wird gedreht
	if direction == False:
		window.blit(pygame.transform.flip(image, True, False), (x, y))


	for event in pygame.event.get():


		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			quit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				direction = True
			elif event.key == pygame.K_d:
				direction = False

	key_pressed_is = pygame.key.get_pressed()

	# Koordinaten update
	if key_pressed_is[K_a]:
		x -= 5
	if key_pressed_is[K_d]: 
		x += 5
	if key_pressed_is[K_w]:
		y -= 5
	if key_pressed_is[K_s]:
		y += 5

	pygame.display.update()