import pygame
pygame.init()

CarWidth = 73
width = 800 
height = 600
GameDisplay = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

CarImg = pygame.image.load('racecar.png')

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

pygame.display.set_caption('Game')


def car(x, y):
	GameDisplay.blit(CarImg, (x, y))

def game_loop():

	x = (width * 0.45)
	y = (height * 0.8)
	x_change = 0
	GameExit = False
	while not GameExit:

		for event in pygame.event.get(): # a list of all events
			if event.type == pygame.QUIT:
				GameExit = True
			if event.type == pygame.KEYDOWN: # not the down arror key, if you're pressing down ANY key
				if event.key == pygame.K_LEFT:
					x_change = -5
				if event.key == pygame.K_RIGHT:
					x_change = 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change

			
		GameDisplay.fill(white)
		car(x, y)

		if x > width - CarWidth  or x < 0:
			GameExit = True

		pygame.display.update()

		clock.tick(70)

game_loop()
pygame.quit()