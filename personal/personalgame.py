import pygame
pygame.init()
window = pygame.display.set_mode((600,600))
pygame.display.set_caption("First Game")
running = True
x = 50
y = 500
velocity = 5
width = 40
height = 40
red = (255, 0, 0)
black = (0, 0, 0)


def draw():
	pygame.time.delay(40)
	window.fill(black)
	pygame.draw.rect(window, red, (x, y, width, height))
	pygame.display.update()
	
	

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and x > 0:
		x-= velocity
	if keys[pygame.K_RIGHT] and x < 600 - width:
		x += velocity
	if keys[pygame.K_DOWN] and y < 600 - height:
		y += velocity
	if keys[pygame.K_UP] and y > 0:
		y -= velocity
	draw()
	
pygame.quit()