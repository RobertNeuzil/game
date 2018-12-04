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

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()