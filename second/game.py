import pygame
def main():

	screenwidth = 600
	screenheight = 500
	rectwidth = 40
	rectheight = 60
	run = True
	positionx = 90
	positiony = 400
	screencolor = (0, 0, 0)
	rectcolor = (255, 0, 0)
	vel = 10



	pygame.init()
	
	pygame.display.set_caption("minimal program")
	screen = pygame.display.set_mode((screenwidth, screenheight))
	

	while run:
		pygame.time.delay(80)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_RIGHT] and positionx < (screenwidth-rectwidth):
			positionx += vel
		if pressed[pygame.K_LEFT] and positionx > 0:
			positionx -= vel

		screen.fill(screencolor)
		
		pygame.draw.rect(screen, rectcolor, (positionx, positiony, rectwidth, rectheight))
		pygame.display.update()
	pygame.quit()

main()


