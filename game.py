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

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('First Game')

screenwidth = 500
x = 50
y = 425
width = 40
height = 60
velocity = 5

run = True
while run:
	
	pygame.time.delay(100)

	for event in pygame.event.get(): # loops through all event to check if they happened
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > velocity:
		x -= velocity

	if keys[pygame.K_RIGHT] and x < screenwidth - width - velocity:
		x += velocity

	if keys[pygame.K_UP] and y > velocity :
		y -= velocity

	if keys[pygame.K_DOWN] and y < screenwidth - height - velocity:
		y += velocity
	
	win.fill((0))
	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	pygame.display.update()

pygame.quit()