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
gray60 = (153, 153, 153)
jumping = False

class rects():
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.jumpcount = 10
	def create(self):
		pygame.draw.rect(window, red, (self.x, self.y, self.width, self.height))
	def create_ground(self):
		pygame.draw.rect(window, gray60, (self.x, self.y, self.width, self.height))


square_one = rects(50, 580 - height, 40, 40)
square_two = rects(210, 400, 150, 20)
square_three  = rects(0, 580, 600, 20)



def draw():
	
	pygame.time.delay(40)
	window.fill(black)
	square_one.create()
	square_two.create()
	square_three.create_ground()
	pygame.display.update()
	
	

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and square_one.x > 0:
		square_one.x-= velocity
	if keys[pygame.K_RIGHT] and square_one.x < 600 - width:
		square_one.x += velocity
	if not (jumping):
		if keys[pygame.K_DOWN] and square_one.y < 600 - height:
			square_one.y += velocity
		if keys[pygame.K_UP] and square_one.y > 0:
			square_one.y -= velocity
		if keys[pygame.K_SPACE]:
			jumping = True
	else:
		if square_one.jumpcount >= -10:
			neg = 1
			if square_one.jumpcount < 0:
				neg = -1
			square_one.y -= (square_one.jumpcount ** 2) * 0.5 * neg
			square_one.jumpcount - 1
		
		else:
			square_one.jumping = True
			square_one.jumpcount = 10
	draw()
	
pygame.quit()