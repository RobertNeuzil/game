import pygame
pygame.init() #necessary
x = 250   # character position
y = 250   # character position
screen_width = 500 # set as variable
screen_height = 500 # set as varaible
width = 40 # character w
height = 40 # character h
vel = 5 # how many pixels the character will "eat" when it moves

run = True # default is True. When false, breaks out of main game loop to quit game
isjump = False # by default, character not jumping
jumpcount = 10

win = pygame.display.set_mode((screen_width, screen_height)) # creating a variable for the display with width/height variables used
pygame.display.set_caption("Game") # will display at top of window

while run: # main game logic loop
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False                   # if, mouse click x, game will exit
	
	keys = pygame.key.get_pressed()  # all keys presses in a list, stored as a 'keys' variable. Finds corresponding key press by searching in list

	if keys[pygame.K_LEFT] and x > vel:
		x -= vel
	if keys[pygame.K_RIGHT] and x < screen_width - width - vel: # you have to subtract the width so the character stops at the first left pixel and remember it is also moving by vel every key press
		x += vel

	if not (isjump):
		if keys[pygame.K_UP] and y > vel:
			y -= vel
		if keys[pygame.K_DOWN]and y < screen_height - height - vel:
			y += vel
		if keys[pygame.K_SPACE]:
			isjump = True
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


	win.fill((0,0,0))    # win variable, black background
	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height) )  # creates the character, more on this in docs
	pygame.display.update() # refreshes the screen. Docs list directions for only refreshing specific parts of the screen to save memory. This refreshes entire screen


pygame.quit()  # when the loop is broken, the kill command is sent