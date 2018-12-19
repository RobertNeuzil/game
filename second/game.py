import pygame
pygame.init()


class Player():
	def __init__(self, width, height, position_x, position_y, char_width, char_height):
		self.width = width
		self.height = height
		self.position_x = position_x
		self.position_y = position_y
		self.screen = pygame.display.set_mode((man.width, man.height))
		self.run = True
		self.black = (0, 0, 0)
		self.red = (255, 0, 0)
		self.char_width = char_width
		self.char_height= char_height


man = Player(500, 500, 50, 450, 30, 30)
man.screen.fill(man.black)
key_press = pygame.event.get()

while man.run:
	pygame.display.update()
	
	for key_press in pygame.event.get():
		if key_press.type == pygame.QUIT:
			man.run = False
	


	pygame.draw.rect((man.screen, man.red, (man.x, man.y, man.char_width, man.char_height))
pygame.quit()