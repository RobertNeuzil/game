import pygame
pygame.init()


width = 800 
height = 600
GameDisplay = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
crashed = False
CarImg = pygame.image.load('racecar.png')

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

pygame.display.set_caption('Game')


def car(x, y):
	GameDisplay.blit(CarImg, (x, y))

x = (width * 0.45)
y = (height * 0.8)


while not crashed:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

	GameDisplay.fill(white)
	car(x, y)
	pygame.display.update()

	clock.tick(60)


pygame.quit()