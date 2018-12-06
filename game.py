import pygame
import sys
pygame.init() # necessary. Docs say you can call individual and initizial individual modules as well. Like font.


x = 50
y = 400
velocity = 5 # velocity will be subtracted/added/multiplied/divided from character to make it move places on screen

SURF_WIDTH = 500     # easier to change later if in variables
SURF_HEIGHT = 500	# easier to change later if in variables

CHAR_WIDTH = 40
CHAR_HEIGHT = 50

RED_RGB = (255, 0, 0)
BLACK_RGB = (0, 0, 0)

isJump = False
jumpCount = 10

window = pygame.display.set_mode((SURF_WIDTH, SURF_HEIGHT)) #sets the size of "window"/ surface
pygame.display.set_caption("First Game") # appears at top of box

run = True
while run:   #main game loop
	pygame.time.delay(100) # delay in miliseconds

	for event in pygame.event.get(): #loops through every event to see if the have or haven't happened
		if event.type == pygame.QUIT: #if you click the x, run is assigned False
			run = False # breaks the loop and goes to pygame.quit()
	
	keys = pygame.key.get_pressed() # a list of keys

	if keys[pygame.K_LEFT] and x > 0:
		x -= velocity
	if keys[pygame.K_RIGHT] and x < SURF_WIDTH - CHAR_WIDTH:
		x += velocity
	if not (isJump):
		if keys[pygame.K_UP] and y > 0:
			y -= velocity
		if keys[pygame.K_DOWN] and y < SURF_HEIGHT - CHAR_HEIGHT:
			y += velocity
		if keys[pygame.K_SPACE]:
			isJump = True
	else:
		if jumpCount >= -10:
			neg = 1
			if jumpCount < 0:
				neg = -1
			y -= (jumpCount ** 2) * 0.5 * neg
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 10
	
	window.fill(BLACK_RGB) # prevnets rectangle from being massive blob

	pygame.draw.rect(window, RED_RGB, (x, y, CHAR_WIDTH, CHAR_HEIGHT) )
	pygame.display.update() # refreshed the game

pygame.quit()