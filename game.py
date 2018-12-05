import pygame # documentation: https://www.pygame.org/docs/
import sys
'''
from docs: Before you can do much with pygame, you will need to initialize it. 
The most common way to do this is just make one call.

This will attempt to initialize all the pygame modules for you.
Not all pygame modules need to be initialized, but this will automatically initialize the ones that do. 

https://www.pygame.org/docs/tut/ImportInit.html
'''
pygame.init()

WIDTH = 800
HEIGHT = 600
RED_RGB = (255,0,0)
player_pos = [400, 300]
player_size = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:  #event types are listed in pygame library https://www.pygame.org/docs/ref/event.html
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == K_LEFT:
				pass
			elif event.key == K_RIGHT:
				pass
	pygame.draw.rect(screen, RED_RGB,  (player_pos[0], player_pos[1], player_size, player_size) )

	pygame.display.update()# a commmand that updates the screen with every iteration THIS IS NECESSARY