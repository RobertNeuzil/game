import pygame
import sys
pygame.init() # necessary. Docs say you can call individual and initizia individual modules as well. Like font.



'''
A list containing the sprites
'''
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png') 

clock = pygame.time.Clock()

x = 50
y = 400
velocity = 5 # velocity will be subtracted/added/multiplied/divided from character to make it move places on screen

SURF_WIDTH = 500     # easier to change later if in variables
SURF_HEIGHT = 480	# easier to change later if in variables

CHAR_WIDTH = 64
CHAR_HEIGHT = 64

RED_RGB = (255, 0, 0)
BLACK_RGB = (0, 0, 0)

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

window = pygame.display.set_mode((SURF_WIDTH, SURF_HEIGHT)) #sets the size of "window"/ surface
pygame.display.set_caption("First Game") # appears at top of box

def redrawGameWindow():
	global walkCount

	window.blit(bg, (0,0))
	if walkCount + 1 >= 27:
		walkCount = 0
	if left:
		window.blit(walkLeft[walkCount//3], (x, y))
		walkCount += 1
	elif right:
		window.blit(walkRight[walkCount//3], (x, y))
		walkCount += 1
	else:
		window.blit(char, (x, y))
	pygame.display.update() # refreshed the game




run = True
while run:   #main game loop
	clock.tick(27)
 
	for event in pygame.event.get(): #loops through every event to see if the have or haven't happened
		if event.type == pygame.QUIT: #if you click the x, run is assigned False
			run = False # breaks the loop and goes to pygame.quit()
	
	keys = pygame.key.get_pressed() # a list of keys

	if keys[pygame.K_LEFT] and x > 0:
		x -= velocity
		left = True
		right = False
	elif keys[pygame.K_RIGHT] and x < SURF_WIDTH - CHAR_WIDTH:
		x += velocity
		left = False
		right = True
	else:
		right = False
		left = False
		walkCount = 0
	
	if not (isJump):  # WHILE NOT JUMPING, DO THIS

		if keys[pygame.K_SPACE]:
			isJump = True
			right = False
			left = False
			walkCount = 0
	else:  # While jumping, do this
		if jumpCount >= -10:
			neg = 1
			if jumpCount < 0:
				neg = -1
			y -= (jumpCount ** 2) * 0.5 * neg
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 10
	
	redrawGameWindow()

pygame.quit()