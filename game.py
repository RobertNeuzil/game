import pygame
pygame.init() #necessary


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

# ^^^^^^^^^^^ Two lists for what image will be loaded when the character is walking left of or right. Some math and variables will be used in game logic to determine where the character is moving

bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')




clock = pygame.time.Clock()




x = 250   # character position
y = 400   # character position
screen_width = 500 # set as variable
screen_height = 480 # set as varaible
width = 64 # character w
height = 64 # character h
vel = 5 # how many pixels the character will "eat" when it moves

run = True # default is True. When false, breaks out of main game loop to quit game
isjump = False # by default, character not jumping
jumpcount = 10

left = False
right = False
walkcount = 0


win = pygame.display.set_mode((screen_width, screen_height)) # creating a variable for the display with width/height variables used
pygame.display.set_caption("Game") # will display at top of window


def RedrawGameWindow():
	global walkcount
	win.blit(bg, (0, 0))    # win variable, black background
	if walkcount + 1 >= 27:
		walkcount = 0
	if left:
		win.blit(walkLeft[walkcount//3], (x, y))
		walkcount += 1
	elif right:
		win.blit(walkRight[walkcount//3], (x, y))
	else:
		win.blit(char, (x,y))

	pygame.display.update() # refreshes the screen. Docs list directions for only refreshing specific parts of the screen to save memory. This refreshes entire screen



while run: # main game logic loop
	clock.tick(27)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False                   # if, mouse click x, game will exit
	
	keys = pygame.key.get_pressed()  # all keys presses in a list, stored as a 'keys' variable. Finds corresponding key press by searching in list

	if keys[pygame.K_LEFT] and x > vel:
		x -= vel
		left = True
		right = False
	elif keys[pygame.K_RIGHT] and x < screen_width - width - vel: # you have to subtract the width so the character stops at the first left pixel and remember it is also moving by vel every key press
		x += vel
		right = True
		left = False
	else:
		right = False
		left = False
		walkcount = 0
	if not (isjump):  # if not False. Character can't move up or down while jumping

		if keys[pygame.K_SPACE]:   # character can't jump while jumping
			isjump = True
			right = False
			left = False
			walkcount = 0
	else:
		if jumpcount >= -10: 
			neg = 1
			if jumpcount < 0:
				neg = -1
			y -= (jumpcount ** 2) * 0.5 * neg
			jumpcount -= 1
		else:
			isjump = False
			jumpcount = 10

	RedrawGameWindow()

pygame.quit()  # when the loop is broken, the kill command is sent