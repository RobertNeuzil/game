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


class rects():
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	def create(self):
		pygame.draw.rect(window, red, (self.x, self.y, self.width, self.height))

square_one = rects(50, 530, 40, 40)
square_two = rects(100, 200, 200, 20)
square_three = rects(100, 300, 150, 20)
square_four = rects(100, 100, 340, 20)
square_five = rects(100, 400, 200, 20)
square_six = rects(60, 300, 150, 20)
def draw():
	pygame.time.delay(40)
	window.fill(black)
	square_one.create()
	square_two.create()
	square_three.create()
	square_four.create()
	square_five.create()
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
	if keys[pygame.K_DOWN] and square_one.y < 600 - height:
		square_one.y += velocity
	if keys[pygame.K_UP] and square_one.y > 0:
		square_one.y -= velocity
	
	draw()
	
pygame.quit()