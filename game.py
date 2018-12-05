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

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Racing Game')
clock = pygame.time.Clock()

crashed = False

while not crashed:
	for event in pygame.event.get():  # creates a list of events for all that happened
		if event.type == pygame.QUIT:
			crashed = True 


	
	pygame.display.update()
	clock.tick(60)

pygame.quit()