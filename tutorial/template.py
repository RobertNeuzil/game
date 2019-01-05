#pygame template - skeleton for new pygame
import pygame
import random

width = 360
height = 480
FPS = 30
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
#Game Loop
running = True
while running:
	# keep loop running at right speed / same speed
	clock.tick(FPS)
	#process input (events)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	#update
	all_sprites.update()	
	
	#draw / render
	screen.fill(black)
	all_sprites.draw(screen)
	# after drawing everything, flip display
	pygame.display.flip()

pygame.quit()