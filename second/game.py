import pygame


class game(object):
	def __init__(self):
		self.screenwidth = 600
		self.screenheight = 500
		self.rectwidth = 40
		self.rectheight = 60
		self.run = True
		self.positionx = 90
		self.positiony = 400
		self.screencolor = (0, 0, 0)
		self.rectcolor = (255, 0, 0)
		self.vel = 10

man = game()
pygame.init()
pygame.display.set_caption("minimal program")
screen = pygame.display.set_mode((man.screenwidth, man.screenheight))
	

while man.run:
	pygame.time.delay(80)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			man.run = False

	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_RIGHT] and man.positionx < (man.screenwidth-man.rectwidth):
		man.positionx += man.vel
	if pressed[pygame.K_LEFT] and man.positionx > 0:
		man.positionx -= man.vel

	screen.fill(man.screencolor)
		
	pygame.draw.rect(screen, man.rectcolor, (man.positionx, man.positiony, man.rectwidth, man.rectheight))
	pygame.display.update()

pygame.quit()




