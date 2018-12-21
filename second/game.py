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
        self.isJump = False
        self.JumpCount = 10


man = game()  # instantiate class on man variable
pygame.init()  # required
pygame.display.set_caption("My Game")  # window title
# the entire surface of the window
screen = pygame.display.set_mode((man.screenwidth, man.screenheight))


while man.run:
    pygame.time.delay(80)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            man.run = False  # breaks out of entire game loop

    # a variable with all possible keypresses. Apply below by calling elements of the list
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and man.positionx < (man.screenwidth - man.rectwidth):
        man.positionx += man.vel
    if pressed[pygame.K_LEFT] and man.positionx > 0:
        man.positionx -= man.vel

    if not(man.isJump):  # if man.isJump == False // If man.isJump does not evaluate to True, run the code
        if pressed[pygame.K_DOWN] and man.positiony < (man.screenheight - man.rectheight):
            man.positiony += man.vel

        if pressed[pygame.K_UP] and man.positiony > 0:
            man.positiony -= man.vel

        if pressed[pygame.K_SPACE]:
            man.isJump = True
    else:
    	if man.JumpCount >= -10:
    		neg = 1
    		if man.JumpCount < 0:
    			neg = -1
    		man.positiony -= (man.JumpCount ** 2) * 0.5 * neg
    		man.JumpCount -= 1

    	else:
    		man.isJump = False
    		man.JumpCount = 10

    screen.fill(man.screencolor)

    pygame.draw.rect(screen, man.rectcolor, (man.positionx,
                                             man.positiony, man.rectwidth, man.rectheight))
    pygame.display.update()

pygame.quit()
